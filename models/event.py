import datetime


class Event:
    def __init__(self, date, name, no_guest, room_local, description, recurring):
        self.date = date
        self.name = name
        self.no_guest = no_guest
        self.room_local = room_local
        self.description = description
        self.recurring = recurring
