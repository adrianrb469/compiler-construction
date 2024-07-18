import sys
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerListener import ConfRoomSchedulerListener

class Event():
    def __init__(self, id, event_name, room, date, start_time, end_time, event_description=None):
        self.id = id
        self.name = event_name
        self.description = event_description
        self.room = room
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Event: {self.name}, id: {self.id}, Room: {self.room}, Description: {self.description}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"

class ConfRoomSchedulerCustomListener(ConfRoomSchedulerListener):

    def __init__(self):
        self.events = []

    def enterReserveStat(self, ctx: ConfRoomSchedulerParser.ReserveStatContext):
        reservation = ctx.reserve()

        event = Event(
            len(self.events) + 1,
            reservation.STRING(0),
            reservation.ID(),
            reservation.DATE(),
            reservation.TIME(0),
            reservation.TIME(1),
            reservation.STRING(1),
        )

        self.events.append(event)

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
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our ConfRoomScheduler grammar, yay!

    semanticchecker = ConfRoomSchedulerCustomListener()
    walker = ParseTreeWalker()
    walker.walk(semanticchecker, tree)


if __name__ == '__main__':
    main(sys.argv)
