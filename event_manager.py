from storage import load_events, save_events
from conflict_checker import check_conflict
from utils import validate_datetime

def add_event(name, date, time, type_, location):
    if not validate_datetime(date, time):
        print("Invalid date/time format.")
        return

    events = load_events()
    if check_conflict(events, date, time):
        print("Conflict detected with another event.")
        return

    event = {
        "id": len(events) + 1,
        "name": name,
        "date": date,
        "time": time,
        "type": type_,
        "location": location or "Not specified"
    }
    events.append(event)
    save_events(events)
    print("Event added successfully.")

def edit_event(event_id, field, value):
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            if field in event:
                event[field] = value
                save_events(events)
                print("Event updated.")
                return
            else:
                print("Invalid field.")
                return
    print("Event not found.")

def delete_event(event_id):
    events = load_events()
    updated = [e for e in events if e["id"] != event_id]
    if len(updated) == len(events):
        print("Event not found.")
    else:
        save_events(updated)
        print("Event deleted.")

def view_events(date=None):
    events = load_events()
    if date:
        events = [e for e in events if e["date"] == date]
    if not events:
        print("No events found.")
        return
    for e in events:
        print(f"ID: {e['id']} | {e['name']} on {e['date']} at {e['time']} ({e['type']}) @ {e['location']}")

def search_events(keyword):
    events = load_events()
    results = [e for e in events if keyword.lower() in e["name"].lower()]
    if not results:
        print("No matching events.")
        return
    for e in results:
        print(f"ID: {e['id']} | {e['name']} on {e['date']} at {e['time']}")