from datetime import datetime

def validate_datetime(date_str, time_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False