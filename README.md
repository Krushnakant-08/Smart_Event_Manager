# 📅 Smart Event Manager CLI

Welcome to the **Smart Event Manager**!  
A powerful, Python-based command-line interface (CLI) tool that helps you schedule, manage, and track your events with ease.  
With a clean modular structure and persistent storage, this project is both efficient and maintainable.  

---

## ✨ Features

- **🗓️ Add, Edit, & Delete Events** – Full CRUD functionality.  
- **👁️ Multiple Views**  
  - **Day View**: See all events scheduled for a specific date.  
  - **All Events View**: List all scheduled events.  
- **🔍 Search Events** – Instantly find events by keyword.  
- **⚠️ Conflict Detection** – Prevents double-booking by detecting overlapping schedules.  
- **💾 Persistent Storage** – Events are stored in `events.json`.  
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
└── events.json         # Database file storing events
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python **3.x**  
- No external dependencies required  

### 2. Setup
Clone or download the project, and ensure all files are in the same directory.  

### 3. Run the Application
Navigate to the project directory in your terminal and run:

```bash
python main.py <command> [options]
```

---

## 💻 Sample CLI Commands

### 1. Add a New Event
```bash
python main.py add --name "Team Standup" --date "21-08-2025" --time "10:00" --type "Work" --location "Online"
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
ID: 1 | Updated Meeting on 20-08-2025 at 14:00 (Work) @ Conference Room
ID: 2 | Family Lunch on 20-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt
ID: 4 | Family Lunch on 21-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt
```

---

### 3. View Events for a Specific Date
```bash
python main.py view --date "20-08-2025"
```
**Output:**
```
ID: 1 | Updated Meeting on 20-08-2025 at 14:00 (Work) @ Conference Room
ID: 2 | Family Lunch on 20-08-2025 at 13:00 (Personal) @ Krishna Veg Restraunt
```

---

### 4. Edit an Event
```bash
python main.py edit --id 1 --field "name" --value "Project Kick-off Meeting"
```
**Output:**
```
Event updated.
```

---

### 5. Search for an Event
```bash
python main.py search --keyword "Lunch"
```
**Output:**
```
ID: 2 | Family Lunch on 20-08-2025 at 13:00
ID: 4 | Family Lunch on 21-08-2025 at 13:00
```

---

### 6. Delete an Event
```bash
python main.py delete --id 3
```
**Output:**
```
Event deleted.
```

---

## 📝 License
This project is open-source and available under the **MIT License**.  

---

## 🙌 Acknowledgments
Thank you for using **Smart Event Manager CLI**! 🎉  
