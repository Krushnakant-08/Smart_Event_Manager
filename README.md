# 📅 Smart Event Manager CLI

Welcome to the **Smart Event Manager**!  
A powerful, Python-based command-line interface (CLI) tool that helps you schedule, manage, and track your events with ease.  
With a clean modular structure and persistent storage, this project is both efficient and maintainable.  

---

## ✨ Features

- **🗓️ Add, Edit, & Delete Events** – Full CRUD functionality.  
- **👁️ Multiple Views**  
  - **Day View**: See all events scheduled for a specific date.  
  - **Today View**: Instantly see events scheduled for today.  
  - **All Events View**: List all scheduled events.  
- **🔍 Search Events** – Instantly find events by keyword.  
- **⚠️ Conflict Detection** – Prevents double-booking by detecting overlapping schedules.  
- **💾 Persistent Storage** – Events are stored in `events.json`.  
- **📧 Email Reminders** – Automatically send reminders to attendees for today’s events.  
- **🧩 Modular Structure** – Code is separated into modules for maintainability and scalability.  

---

## 📂 Project Structure

```
/smart-event-manager
│
├── main.py             # Entry point of the application
├── cli.py              # Defines the command-line interface (argparse)
├── event_manager.py    # Core logic for event operations
├── storage.py          # Handles reading/writing JSON data
├── utils.py            # Utility functions (date/time validation, etc.)
├── conflict_checker.py # Scheduling conflict detection logic
├── reminder.py         # Sends email reminders for today’s events
├── attendees.xlsx      # List of attendee emails
└── events.json         # Database file storing events
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python **3.x**  
- No external dependencies required for event manager core  
- For email reminders:  
  - `pandas`, `openpyxl`, and `python-dotenv` must be installed  
  ```bash
  pip install pandas openpyxl python-dotenv
  ```

### 2. Setup
- Clone or download the project.  
- Create a **`.env`** file in the root directory with your SMTP credentials:  
  ```ini
  SENDER_EMAIL=youremail@example.com
  APP_PASSWORD=your_app_password
  SMTP_SERVER=smtp.gmail.com
  SMTP_PORT=465
  ```  
- Create **`attendees.xlsx`** with at least one column:  
  | Email |
  |-------|
  | attendee1@example.com |
  | attendee2@example.com |

### 3. Run the Application
Navigate to the project directory in your terminal and run:

```bash
python main.py <command> [options]
```

To send reminders manually:
```bash
python reminder.py
```

---

## 💻 Sample CLI Commands

### 1. Add a New Event
```bash
python main.py add --name "Project Demo" --date "18-08-2025" --time "15:00" --type "Work" --location "Main Auditorium"
python main.py add --name "Doctor's Appointment" --date "19-08-2025" --time "11:30" --type "Personal"
python main.py add --name "Client Call" --date "20-08-2025" --time "14:00" --type "Work"
```
**Output:**
```
Event added successfully.
```

---

### 2. View All Events
```bash
python main.py view
```
**Output:**
```
ID: 1 | Project Demo on 18-08-2025 at 15:00 (Work) @ Online Meeting Room
ID: 2 | Doctor's Appointment on 19-08-2025 at 11:30 (Personal) @ Not specified
ID: 3 | Client Call on 20-08-2025 at 14:00 (Work) @ Not specified
```

---

### 3. View Events for a Specific Date
```bash
python main.py view --date "19-08-2025"
```
**Output:**
```
ID: 2 | Doctor's Appointment on 19-08-2025 at 11:30 (Personal) @ Not specified
```

---

### 4. View Today's Events
```bash
python main.py view --date "today"
```
**Output:**
```
ID: 1 | Project Demo on 18-08-2025 at 15:00 (Work) @ Online Meeting Room
```
*(Example output if today's date is 18-08-2025)*

---

### 5. Edit an Event
```bash
python main.py edit --id 1 --field "name" --value "Project Kick-off Demo"
```
**Output:**
```
Event updated.
```

---

### 6. Search for an Event
```bash
python main.py search --keyword "Call"
```
**Output:**
```
ID: 3 | Client Call on 20-08-2025 at 14:00
```

---

### 7. Delete an Event
```bash
python main.py delete --id 2
```
**Output:**
```
Event deleted.
```

---

### 8. Send Email Reminders
```bash
python reminder.py
```
**Output:**
```
Found 1 event(s) for today and 2 attendee(s).

--- Sending reminders for: 'Project Demo' at 15:00 ---
  -> Successfully sent reminder to: attendee1@example.com
  -> Successfully sent reminder to: attendee2@example.com

All reminders have been processed.
```

---

## 🙌 Acknowledgments
Thank you for using **Smart Event Manager CLI**! 🎉  
