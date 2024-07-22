import datetime
import schedule
import time
import threading
import pytz
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerListener import ConfRoomSchedulerListener

CENTRAL = pytz.timezone("America/Guatemala")

eventsDB = []


class Event:
    def __init__(
        self,
        id,
        person_name,
        event_name,
        room,
        date,
        start_time,
        end_time,
        type="Meeting",
        event_description=None,
    ):
        self.id = id
        self.person_name = person_name
        self.name = event_name
        self.type = type
        self.description = event_description
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (
            f"Event: {self.name}, ID: {self.id}, Type: {self.type} Room: {self.room}, Person: {self.person_name}, "
            f"Description: {self.description}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"
        )

    def overlaps_with(self, other_event, rescheduling=False):
        # If rescheduling, allow the same event to be rescheduled
        if rescheduling and self.id == other_event.id:
            return False
        if self.room != other_event.room or self.date != other_event.date:
            return False

        start1 = datetime.datetime.strptime(self.start_time, "%H:%M").replace(
            tzinfo=CENTRAL
        )
        end1 = datetime.datetime.strptime(self.end_time, "%H:%M").replace(
            tzinfo=CENTRAL
        )
        start2 = datetime.datetime.strptime(other_event.start_time, "%H:%M").replace(
            tzinfo=CENTRAL
        )
        end2 = datetime.datetime.strptime(other_event.end_time, "%H:%M").replace(
            tzinfo=CENTRAL
        )

        return start1 < end2 and start2 < end1

    def notification_time(self, minutes_before=30):
        event_datetime = datetime.datetime.strptime(
            f"{self.date} {self.start_time}", "%d/%m/%Y %H:%M"
        )
        event_datetime = CENTRAL.localize(event_datetime)
        return event_datetime - datetime.timedelta(minutes=minutes_before)


# Global notification function
def notify_event(event):
    print(
        f"Notification: Event '{event.name}' is starting soon. (Person: {event.person_name}, Room: {event.room}, Date: {event.date}, Start Time: {event.start_time})"
    )


class ConfRoomSchedulerCustomListener(ConfRoomSchedulerListener):

    def __init__(self):
        global eventsDB
        self.events = eventsDB

    def enterReserveStat(self, ctx: ConfRoomSchedulerParser.ReserveStatContext):
        reservation = ctx.reserve()

        new_event = Event(
            len(self.events) + 1,
            reservation.NAME().getText(),
            reservation.STRING(0).getText().strip('"'),
            reservation.ID().getText(),
            reservation.DATE().getText(),
            reservation.TIME(0).getText(),
            reservation.TIME(1).getText(),
            (
                reservation.STRING(1).getText().strip('"')
                if reservation.STRING(1)
                else "Metting"
            ),
            (
                reservation.STRING(2).getText().strip('"')
                if reservation.STRING(2)
                else None
            ),
        )

        # Check for invalid date
        new_event_date = datetime.datetime.strptime(new_event.date, "%d/%m/%Y")
        new_event_date = new_event_date.replace(tzinfo=CENTRAL)
        if new_event_date < datetime.datetime.now(CENTRAL):
            print(f"Error: Event '{new_event.name}' has a past date.")
            return

        # Check for invalid start and end times
        if datetime.datetime.strptime(
            new_event.start_time, "%H:%M"
        ) >= datetime.datetime.strptime(new_event.end_time, "%H:%M"):
            print(
                f"Error: Event '{new_event.name}' has an end time that is earlier than its start time."
            )
            return

        # Maximum event duration is 4 hours
        if (
            datetime.datetime.strptime(new_event.end_time, "%H:%M")
            - datetime.datetime.strptime(new_event.start_time, "%H:%M")
        ).seconds > 4 * 60 * 60:
            print(
                f"Error: Event '{new_event.name}' exceeds the maximum duration of 4 hours."
            )
            return

        # Check for overlapping events
        for event in self.events:
            if event.overlaps_with(new_event):
                print(
                    f"Error: Event '{new_event.name}' overlaps with existing event '{event.name}' in room '{new_event.room}' on '{new_event.date}'."
                )
                return

        self.events.append(new_event)

        # Schedule notification
        notification_time = new_event.notification_time()
        adjusted_notification_time = notification_time - datetime.timedelta(days=1)
        if notification_time < datetime.datetime.now(CENTRAL):
            notify_event(new_event)
        else:
            schedule_time_str = adjusted_notification_time.strftime(
                "%Y-%m-%d %H:%M:%S %Z%z"
            )
            print(
                f"Scheduling notification for event '{new_event.name}' at {schedule_time_str}"
            )
            schedule.every().day.at(adjusted_notification_time.strftime("%H:%M")).do(
                notify_event, new_event
            )

        for e in self.events:
            print(e.__str__())
        print()

    def enterCancelStat(self, ctx: ConfRoomSchedulerParser.CancelStatContext):
        eventId = int(ctx.cancel().INT().getText())
        event = None
        for e in self.events:
            if e.id == eventId:
                event = e
                self.events.remove(e)
                print(f"Event {event.name} has been cancelled.")
                break

        if event is None:
            print(f"Event does not exist.")
            return

        print()
        for e in self.events:
            print(e.__str__())
        print()

    def enterListStat(self, ctx: ConfRoomSchedulerParser.ListStatContext):
        print("\n--- EVENTS ---")
        for index, e in enumerate(self.events):
            print(f"{index+1}) {e.__str__()}")
        print()

    def enterRescheduleStat(self, ctx: ConfRoomSchedulerParser.RescheduleStatContext):
        reschedule = ctx.reschedule()

        eventId = int(reschedule.INT().getText())
        new_date = reschedule.DATE().getText()
        new_start_time = reschedule.TIME(0).getText()
        new_end_time = reschedule.TIME(1).getText()

        event = None
        for e in self.events:
            if e.id == eventId:
                event = e
                break

        if event is None:
            print(f"Error: Event with ID '{eventId}' does not exist.")
            return

        # Check for invalid date
        new_event_date = datetime.datetime.strptime(new_date, "%d/%m/%Y")
        new_event_date = new_event_date.replace(tzinfo=CENTRAL)
        if new_event_date < datetime.datetime.now(CENTRAL):
            print(f"Error: Event '{event.name}' has a past date.")
            return

        # Check for invalid start and end times
        if datetime.datetime.strptime(
            new_start_time, "%H:%M"
        ) >= datetime.datetime.strptime(new_end_time, "%H:%M"):
            print(
                f"Error: Event '{event.name}' has an end time that is earlier than its start time."
            )
            return

        # Maximum event duration is 4 hours
        if (
            datetime.datetime.strptime(new_end_time, "%H:%M")
            - datetime.datetime.strptime(new_start_time, "%H:%M")
        ).seconds > 4 * 60 * 60:
            print(
                f"Error: Event '{event.name}' exceeds the maximum duration of 4 hours."
            )
            return

        # Create a temporary event for overlap checking
        temp_event = Event(
            id=eventId,
            person_name=event.person_name,
            event_name=event.name,
            room=event.room,
            date=new_date,
            start_time=new_start_time,
            end_time=new_end_time,
            type=event.type,
            event_description=event.description,
        )

        # Check for overlapping events
        for e in self.events:
            if e.overlaps_with(temp_event, True):
                print(
                    f"Error: Event '{event.name}' overlaps with existing event '{e.name}' in room '{event.room}' on '{event.date}'."
                )
                return

        # Update event details
        event.date = new_date
        event.start_time = new_start_time
        event.end_time = new_end_time

        # Schedule notification
        notification_time = event.notification_time()
        adjusted_notification_time = notification_time - datetime.timedelta(days=1)
        if notification_time < datetime.datetime.now(CENTRAL):
            notify_event(event)
        else:
            schedule_time_str = adjusted_notification_time.strftime(
                "%Y-%m-%d %H:%M:%S %Z%z"
            )
            print(
                f"Scheduling notification for event '{event.name}' at {schedule_time_str}"
            )


# Run the schedule in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        # print("next notification at:", schedule.next_run())
        time.sleep(5)


# Start the schedule in a separate thread
schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.daemon = True
schedule_thread.start()


def process_input(input_text):
    input_stream = InputStream(input_text)
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()

    semanticchecker = ConfRoomSchedulerCustomListener()
    walker = ParseTreeWalker()
    walker.walk(semanticchecker, tree)


def interactive_shell():
    print("Enter your commands:")
    while True:
        try:
            input_text = input(">> ").strip()
            if input_text == "":
                continue
            elif input_text == "exit":
                break
            process_input(input_text)
        except EOFError:
            break


if __name__ == "__main__":
    interactive_shell()
