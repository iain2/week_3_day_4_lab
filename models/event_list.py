from models.event import *
import datetime

event1 = Event(
    # datetime.date(2022, 5, 19),
    "5/10/2022",
    "Charity Function",
    100,
    "Events hall",
    "Black tie, full catering",
    False,
)
event2 = Event(
    # datetime.date(2022, 7, 24),
    "24/7/2022",
    "Conference",
    50,
    "Events hall",
    "Corporate event, drinks and appertisers",
    True,
)
event3 = Event(
    # datetime.date(2022, 5, 17),
    "22/09/2022",
    "Bussiness meeting",
    10,
    "Conference room 1",
    "T/C",
    True,
)

events_list = [event1, event2, event3]


def add_new_event(event):
    events_list.append(event)
