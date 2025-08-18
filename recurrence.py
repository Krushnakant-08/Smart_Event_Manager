from datetime import datetime, timedelta

def get_next_occurrence(event):

    recurrence = event.get("recurrence", "Not recurring").lower()
    if recurrence not in ("monthly", "weekly", "daily"):
        return None
    event_date = datetime.strptime(event["date"], "%d-%m-%Y")
    if recurrence == "monthly":
        month = event_date.month + 1
        year = event_date.year
        if month > 12:
            month = 1
            year += 1
        try:
            next_date = event_date.replace(year=year, month=month)
        except ValueError:
            next_date = event_date.replace(year=year, month=month, day=1)
    elif recurrence == "weekly":
        next_date = event_date + timedelta(weeks=1)
    elif recurrence == "daily":
        next_date = event_date + timedelta(days=1)
    return next_date.strftime("%d-%m-%Y")


def auto_add_next_occurrences(events):

    max_id = max((e["id"] for e in events), default=0)
    added = False
    for event in events[:]:
        next_date = get_next_occurrence(event)
        if next_date:
            if not any(e["name"].lower() == event["name"].lower() and e["date"] == next_date and e["time"] == event["time"] for e in events):
                new_event = event.copy()
                new_event["date"] = next_date
                max_id += 1
                new_event["id"] = max_id
                events.append(new_event)
                added = True
    return added
