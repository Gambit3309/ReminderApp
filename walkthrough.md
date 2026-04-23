# 📋 Reminder App — Progress Summary
*Last updated: 2026-04-23*

---

## 🎯 Project Overview

**What you're building:** A full-featured Reminder App in Python with recurring background pings and desktop notifications.

**Your background:** 4th semester SE student. Strong in C++. Learning Python for the first time.

**Mentor rule:** You write all code. Mentor reviews, explains, and guides only.

**End goal:** Complete Python app → then port to Flutter for mobile.

---

## 📐 App Specification

### Standard Features
| Feature | Description |
|---------|-------------|
| Add Reminder | Enter title, description, due date & time, priority level |
| View Reminders | Display all reminders with status indicators (pending / done / overdue) |
| Edit Reminder | Update any field of an existing reminder by ID |
| Delete Reminder | Remove a reminder by its number in the list |
| Mark as Done | Flag a reminder as completed ✅ |
| Search | Find reminders by keyword in title or description |
| Filter | Show only `pending`, `done`, or `overdue` reminders |
| Sort | Sort by due date (earliest first) or by priority |

### ⭐ Advanced Feature — Recurring Background Pings
| Aspect | Detail |
|--------|--------|
| What it does | Reminds the user every X minutes before the due date |
| How it works | A background thread runs silently alongside the main app |
| Trigger | If a reminder's ping interval has elapsed and due date hasn't passed → fire notification |
| Stop condition | Stops pinging once reminder is marked done or due date has passed |
| Notification type | Real Windows desktop toast notification via `plyer` library |

### 🛠️ Tech Stack
| Component | Technology |
|-----------|-----------|
| Language | Python 3.10+ |
| Interface | CLI (Command Line Interface) |
| Storage | JSON file (`reminders.json`) |
| Background pings | `threading` module (built-in) |
| Desktop notifications | `plyer` (third-party, `pip install plyer`) |
| Date/time handling | `datetime` module (built-in) |
| Unique IDs | `uuid` module (built-in) |

### 📦 Data Model (Per Reminder)
```python
{
    "id":               "uuid-string",        # Unique identifier
    "title":            "Quiz Prep",          # Short title
    "description":      "Study chapters 1-3", # Details
    "priority":         "high",               # high / medium / low
    "created_at":       "2026-04-18 20:05",   # Auto-stamped on creation
    "due_at":           "2026-04-20 14:00",   # User-provided due date & time
    "is_done":          False,                # Marked done by user
    "ping_interval_mins": 30                  # None = no pings, int = ping every X mins
}
```

### 📁 Project File Structure (Final)
```
ReminderApp/
├── main.py              ← Entry point, menu loop
├── models/
│   └── task.py          ← Reminder class definition
├── task_manager.py      ← ReminderManager class (add/delete/search/sort/save/load)
├── reminder_engine.py   ← Background ping thread logic
├── database.py          ← JSON file read/write logic
├── notifier.py          ← Desktop notification wrapper (plyer)
├── utils/               ← Helper utilities (input validation, formatting)
└── reminders.json       ← Auto-generated data file (not committed to git)
```

---

## ✅ Milestone 1 — Hello Python (Complete)

### What You Built
- A CLI menu system that loops forever using `while True`
- User selects numbered options from a printed menu
- App responds with placeholder messages for each choice

### Python Concepts Learned

| Concept | What It Is | C++ Equivalent |
|---------|-----------|----------------|
| `print()` | Output to console | `cout <<` |
| `input()` | Read user input as string | `cin >>` |
| f-strings | `f"Hello {name}"` | `printf` / string concat |
| `while True:` | Infinite loop | `while(true)` |
| `break` | Exit a loop | `break` |
| Indentation | Defines code blocks (no `{}`) | `{ }` braces |
| No `int main()` | Python runs top-to-bottom | Required in C++ |

### Key Insight
Python has no type declarations. No `string name`, no `int choice` — variables just exist when you assign them. Python figures out the type dynamically at runtime.

---

## ✅ Milestone 2 — Lists, Loops & First Function (Complete)

### What You Built
- Reminders stored in a **list** (`reminder_list`)
- Menu displayed by **looping** over a list using `enumerate()`
- **Add Reminder:** takes title + description, appends to list
- **View Reminders:** loops and prints all items with numbers
- **Delete Reminder:** shows list, asks for number, removes item
- **Exit:** breaks the loop
- First function: `view_reminder_list()` extracted from the loop

### Python Concepts Learned

| Concept | What It Is | C++ Equivalent |
|---------|-----------|----------------|
| `list = []` | Dynamic array | `vector<string>` |
| `.append(x)` | Add to end of list | `.push_back(x)` |
| `.pop(i)` | Remove item at index | `.erase(v.begin()+i)` |
| `for x in list:` | Iterate over list | range-based for |
| `enumerate(list, start=1)` | Loop with index+value | `for(int i=0; ...)` |
| `if not list:` | Check if list is empty | `if(v.empty())` |
| `match/case` | Pattern matching switch | `switch/case` |
| `def func():` | Define a function | `void func()` |

### Notable Decisions
- Used `match/case` (Python 3.10+) instead of `if/elif` chain — a modern Python feature
- Used `enumerate(menu, start=1)` so numbering starts at 1 (not 0) — cleaner UX
- Stored reminders as plain strings (`"title | description"`)

---

## ✅ Milestone 3 — Full Refactor + `datetime` (Complete)

### What You Built
- **All logic moved into named functions:** `add_reminder()`, `view_reminders()`, `delete_reminder()`
- **`main()` function created** — contains the `while True` loop
- **`if __name__ == "__main__": main()`** guard added at the bottom
- **`datetime` module imported** — creation timestamp auto-stamped on every reminder
- **Due date input** added to `add_reminder()`

### Python Concepts Learned

#### The `datetime` Module
```python
from datetime import datetime

now = datetime.now()
creation_date = now.strftime("%Y-%m-%d %H:%M")
```
- `datetime.now()` → gives current date and time as a `datetime` object
- `.strftime()` → formats it as a readable string ("string format time")
- Format codes: `%Y` = 4-digit year, `%m` = month, `%d` = day, `%H` = hour (24h), `%M` = minutes

#### The `__name__` Guard
```python
if __name__ == "__main__":
    main()
```
Every Python file has a hidden variable `__name__`. Python sets it to:
- `"__main__"` → when you run the file directly (`python main.py`)
- `"main"` → when another file imports it (`import main`)

This guard ensures `main()` only runs when the file is executed directly — not when imported by another module. This becomes critical in M7 when you split into multiple files.

#### Modules & Imports
- `from datetime import datetime` — imports only the `datetime` class from the `datetime` module
- Python's standard library has hundreds of built-in modules (no installation needed)

### Bugs Found & Fixed

#### Bug 1 — Wrong `strftime` format codes
```python
# ❌ Wrong
now.strftime("%Y-%M-%D %H:%M")
# %M = Minutes (not month!), %D = doesn't exist in Python

# ✅ Fixed
now.strftime("%Y-%m-%d %H:%M")
# %m = month, %d = day
```
**Lesson:** Python's strftime is case-sensitive. Uppercase `%M` = Minutes. Lowercase `%m` = Month.

#### Bug 2 — `main()` function never created
Added `if __name__ == "__main__": main()` but forgot to wrap the `while` loop in `def main():`. Python would crash with `NameError: name 'main' is not defined`.

**Lesson:** The `__name__` guard is useless without an actual `main()` function. The entry point and the guard must both exist.

---

## 📄 Current State of `main.py`

```python
from datetime import datetime

menu = ["Add Reminder", "View Reminders", "Delete Reminder", "Exit"]
reminder_list = []

def view_reminders():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        for index, reminder in enumerate(reminder_list, start=1):
            print(f'{index}. {reminder}')

def add_reminder():
    title = input("Enter Title:")
    desc = input("Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    now = datetime.now()
    creation_date = now.strftime("%Y-%m-%d %H:%M")
    user_input = title + ' | ' + desc + '\n' + "Due Date: " + due_date + '\nAdded: ' + creation_date
    reminder_list.append(user_input)
    print("Reminder Added")

def delete_reminder():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        view_reminders()
        del_reminder = input("Enter reminder number: ")
        removed = reminder_list.pop(int(del_reminder)-1)
        print(f"'{removed}' has been deleted!")

def main():
    while True:
        print()
        print("My Custom Reminder App")
        for index, item in enumerate(menu, start=1):
            print(f'{index}. {item}')

        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                add_reminder()
            case "2":
                view_reminders()
            case "3":
                delete_reminder()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option, try again.")

if __name__ == "__main__":
    main()
```

---

## 🔲 What's Coming Next — Milestone 4: Dictionaries & Data Modeling

Currently reminders are stored as raw strings like:
```
"Quiz | Study ch1-3\nDue Date: 2026-04-20\nAdded: 2026-04-18 20:05"
```

This is fragile. You can't easily *search*, *sort*, or *mark as done* on a plain string.

In M4 you'll replace this with **dictionaries** — the Python equivalent of a `struct`:
```python
{
    "id": "some-unique-id",
    "title": "Quiz",
    "description": "Study ch1-3",
    "priority": "high",
    "created_at": "2026-04-18 20:05",
    "due_at": "2026-04-20 14:00",
    "is_done": False,
    "ping_interval_mins": None
}
```

New features added in M4:
- Mark reminder as Done ✅
- Edit a reminder
- Priority levels (high / medium / low)
- Find reminder by ID

---

## 📍 Milestone Tracker

| Milestone | Status |
|-----------|--------|
| 1 — Hello Python | ✅ Complete |
| 2 — Lists, Loops & Functions | ✅ Complete |
| 3 — Full Refactor + datetime | ✅ Complete |
| 4 — Dictionaries & Data Model | 🔲 Up Next |
| 5 — File I/O & JSON | 🔲 Not Started |
| 6 — Search, Filter, Sort | 🔲 Not Started |
| 7 — OOP Refactor | 🔲 Not Started |
| 8 — Recurring Pings (Threading) | 🔲 Not Started |
| 9 — Notifications & Polish | 🔲 Not Started |
