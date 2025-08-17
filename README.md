📅 Smart Event Manager CLI
Welcome to the Smart Event Manager! This is a powerful, command-line interface (CLI) application built with Python to help you effortlessly schedule, manage, and track your events. Designed with a clean, modular architecture, this tool is both efficient and easy to use.

✨ Core Features
This project implements all the mandatory features required for a robust event management system:

🗓️ Add, Edit, & Delete Events: Full CRUD (Create, Read, Update, Delete) functionality for your events.

👁️ Multiple View Options:

Day View: See all events scheduled for a specific date.

All Events View: Get a complete list of all your scheduled events.

🔍 Powerful Search: Instantly find events by a keyword in the event's name.

⚠️ Conflict Detection: The system automatically checks for scheduling conflicts at the same date and time to prevent double-booking.

💾 Persistent Storage: Your events are safely stored in a events.json file, so you never lose your data.

🧩 Modular Structure: The source code is organized into logical modules (cli, event_manager, storage, utils) for better readability, maintenance, and scalability.

📂 Project Structure
The project follows a modular structure to separate concerns and make the codebase clean and maintainable.

/smart-event-manager
│
├── main.py             # Entry point of the application
├── cli.py              # Defines the command-line interface (using argparse)
├── event_manager.py    # Contains the core logic for event operations
├── storage.py          # Handles data persistence (reading/writing to JSON file)
├── utils.py            # Utility functions (e.g., date/time validation)
├── conflict_checker.py # Logic to detect scheduling conflicts
└── events.json         # The database file where events are stored

🚀 How to Run the Project
Getting the Smart Event Manager up and running is simple. Just follow these steps:

1. Prerequisites
Make sure you have Python 3.x installed on your system. No external libraries are needed.

2. Setup
Ensure all the project files (main.py, cli.py, etc.) are in the same directory.

3. Run from the Command Line
Navigate to the project's root directory in your terminal and use python main.py followed by the desired command and its arguments.

💻 Sample CLI Commands
Here are some examples of how to interact with the Smart Event Manager from your terminal.

1. Add a New Event
To schedule a new event. The --location argument is optional.

python main.py add --name "Team Standup" --date "21-08-2025" --time "10:00" --type "Work" --location "Online"

Output:

Event added successfully.

2. View All Events
To see a list of all scheduled events.

python main.py view

Output:

ID: 1 | Updated Meeting on 20-08-2025 at 14:00 (Work) @ Conference Room
ID: 2 | Family Lunch on 20-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt
ID: 4 | Family Lunch on 21-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt

3. View Events for a Specific Date
To filter events for a particular day.

python main.py view --date "20-08-2025"

Output:

ID: 1 | Updated Meeting on 20-08-2025 at 14:00 (Work) @ Conference Room
ID: 2 | Family Lunch on 20-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt

4. Edit an Existing Event
To modify the details of an event using its ID.

python main.py edit --id 1 --field "name" --value "Project Kick-off Meeting"

Output:

Event updated.

5. Search for an Event
To find an event by a keyword (case-insensitive).

python main.py search --keyword "Lunch"

Output:

ID: 2 | Family Lunch on 20-08-2025 at 13:00
ID: 4 | Family Lunch on 21-08-2025 at 13:00

6. Delete an Event
To remove an event from the schedule using its ID.

python main.py delete --id 3

Output:

Event deleted.

Thank you for using the Smart Event Manager!