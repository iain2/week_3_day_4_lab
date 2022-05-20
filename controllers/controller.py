from flask import render_template, request
from app import app
from models.event_list import events_list, add_new_event
from models.event import Event


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events_list=events_list)


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    event_no_guests = request.form["guests"]
    event_room_location = request.form["room"]
    event_description = request.form["description"]
    event_recuring = request.form["recurring"]
    new_event = Event(
        event_date,
        event_name,
        event_no_guests,
        event_room_location,
        event_description,
        event_recuring,
    )
    add_new_event(new_event)

    return render_template("index.html", title="Home", events_list=events_list)
