import argparse
from event_manager import add_event, edit_event, delete_event, view_events, search_events

def run_cli():
    parser = argparse.ArgumentParser(description="Smart Event Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Event
    add = subparsers.add_parser("add", help="Add a new event")
    add.add_argument("--name", required=True)
    add.add_argument("--date", required=True, help="Format: DD-MM-YYYY")
    add.add_argument("--time", required=True, help="Format: HH:MM")
    add.add_argument("--type", required=True)
    add.add_argument("--location", required=False)

    # Edit Event
    edit = subparsers.add_parser("edit", help="Edit an existing event")
    edit.add_argument("--id", type=int, required=True)
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

    args = parser.parse_args()

    if args.command == "add":
        add_event(args.name, args.date, args.time, args.type, args.location)
    elif args.command == "edit":
        edit_event(args.id, args.field, args.value)
    elif args.command == "delete":
        delete_event(args.id)
    elif args.command == "view":
        view_events(args.date)
    elif args.command == "search":
        search_events(args.keyword)