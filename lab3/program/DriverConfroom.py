import datetime
import sys
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerListener import ConfRoomSchedulerListener


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
        event_description=None,
    ):
        self.id = id
        self.person_name = person_name
        self.name = event_name
        self.description = event_description
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (
            f"Event: {self.name}, ID: {self.id}, Room: {self.room}, Person: {self.person_name}, "
            f"Description: {self.description}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"
        )

    def overlaps_with(self, other_event):
        if self.room != other_event.room or self.date != other_event.date:
            return False

        start1 = datetime.datetime.strptime(self.start_time, "%H:%M")
        end1 = datetime.datetime.strptime(self.end_time, "%H:%M")
        start2 = datetime.datetime.strptime(other_event.start_time, "%H:%M")
        end2 = datetime.datetime.strptime(other_event.end_time, "%H:%M")

        return start1 < end2 and start2 < end1


class ConfRoomSchedulerCustomListener(ConfRoomSchedulerListener):

    def __init__(self):
        self.events = []

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
                else None
            ),
        )

        # Check for overlapping events
        for event in self.events:
            if event.overlaps_with(new_event):
                print(
                    f"Error: Event '{new_event.name}' overlaps with existing event '{event.name}' in room '{new_event.room}' on '{new_event.date}'."
                )
                return

        self.events.append(new_event)

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


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = (
        parser.prog()
    )  # We are using 'prog' since this is the starting rule based on our ConfRoomScheduler grammar, yay!

    semanticchecker = ConfRoomSchedulerCustomListener()
    walker = ParseTreeWalker()
    walker.walk(semanticchecker, tree)


if __name__ == "__main__":
    main(sys.argv)
