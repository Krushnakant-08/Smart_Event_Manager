import argparse
from event_manager import add_event, edit_event, delete_event, view_events, search_events
from reminder import send_event_reminders

def run_cli():
    parser = argparse.ArgumentParser(description="Smart Event Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Event
    add = subparsers.add_parser("add", help="Add a new event")
    add.add_argument("--name", required=True)
    add.add_argument("--date", required=True, help="Format: DD-MM-YYYY")
    add.add_argument("--time", required=True, help="Format: HH:MM")
    add.add_argument("--type", required=True)
    add.add_argument("--recurrence", required=False, help="Recurrence pattern (e.g., daily, weekly, monthly)")
    add.add_argument("--location", required=False)

    # Edit Event
    edit = subparsers.add_parser("edit", help="Edit an existing event")
    group = edit.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", type=int, help="Event ID")
    group.add_argument("--name", type=str, help="Event name")
    edit.add_argument("--field", required=True)
    edit.add_argument("--value", required=True)

    # Delete Event
    delete = subparsers.add_parser("delete", help="Delete an event")
    delete.add_argument("--id", type=int, required=True)

    # View Events
    view = subparsers.add_parser("view", help="View all events or by date")
    view.add_argument("--date", required=False)

    # Search Events
    search = subparsers.add_parser("search", help="Search events by keyword")
    search.add_argument("--keyword", required=True)


    # Remind (send event reminders)
    remind = subparsers.add_parser("remind", help="Send reminder emails for today's events")

    args = parser.parse_args()

    if args.command == "add":
        add_event(args.name, args.date, args.time, args.type, args.location, args.recurrence)
    elif args.command == "edit":
        if args.id is not None:
            edit_event(args.id, args.field, args.value)
        else:
            edit_event(args.name, args.field, args.value)
    elif args.command == "delete":
        delete_event(args.id)
    elif args.command == "view":
        view_events(args.date)
    elif args.command == "search":
        search_events(args.keyword)
    elif args.command == "remind":
        send_event_reminders()