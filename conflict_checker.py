def check_conflict(events, date, time):
    for event in events:
        if event["date"] == date and event["time"] == time:
            return True
    return False