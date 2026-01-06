# 🧠 AI-Native Advanced Todo Console App  
### Console → Cloud Journey (Phase-1)

A powerful **Python-based interactive Todo Console Application**, designed as **Phase-1** of the  
**Todo App: Console → Cloud (GIAIC Hackathon Project)**.

This phase focuses on:
- Clean architecture
- Business-logic testing
- Rich interactive CLI
- AI-native development practices

---

## 📂 Project Location


phase1_console/
└── phase1_todo/
├── app/
├── tests/
├── requirements.txt
└── README.md


---

## ▶️ 1. How to RUN the Console Todo App

### Step 1: Navigate to the correct directory

```bash
cd phase1_console\phase1_todo

## Step 2: Run the application (Recommended)
python -m app.cli

## Alternative (Direct Run)
python app\cli.py

## ❓ 2. How to Open HELP / MENU

This app uses an interactive menu system.
When you run the app, the main menu automatically appears:

═══════════════════════════════════════════
   📋 AI-Native Advanced Todo Console App
═══════════════════════════════════════════

[1] ➕ Add Task
[2] ❌ Delete Task
[3] ✏️ Update Task
[4] 📋 View Tasks
[5] ✅ Mark Complete
[6] 🔍 Search Tasks
[7] 📊 Task Summary
[0] 🚪 Exit


### 👉 All commands are visible inside the menu — no extra help command required.
🧭 3. All User Commands Supported
Menu Option	Number	Description
➕ Add Task	1	Create a new task with title, description, priority & due date
❌ Delete Task	2	Remove a task (with confirmation)
✏️ Update Task	3	Edit title, description, priority, or due date
📋 View Tasks	4	Display all tasks with sorting
✅ Mark Complete	5	Toggle task status (Pending ↔ Completed)
🔍 Search Tasks	6	Search by keyword, priority, or status
📊 Task Summary	7	View statistics & overview
🚪 Exit	0	Quit the application

##🧪 4. Example Usage (Step-by-Step)
➕ Add Task
Your choice: 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Enter priority (High/Medium/Low, default Medium): High
Enter due date (YYYY-MM-DD, optional): 2026-01-10

❌ Delete Task
Your choice: 2
Enter task ID to delete: 1
Are you sure you want to delete 'Buy groceries'? (y/n): y

✏️ Update Task
Your choice: 3
Enter task ID to update: 1

[1] Title
[2] Description
[3] Priority
[4] Due Date
[0] Cancel
Your choice: 1
Enter new title: Buy weekly groceries

📋 View Tasks
Your choice: 4
Sort by:
[1] Priority
[2] Due Date
[3] Creation Date
Your choice: 1

✅ Mark Complete
Your choice: 5
Enter task ID to toggle: 1

🔍 Search Tasks
Your choice: 6
[1] Keyword
[2] Priority
[3] Status
Your choice: 1
Enter keyword: groceries

📊 Task Summary
Your choice: 7

🧪 5. How to RUN TESTS (pytest)
Run all tests
pytest tests/

Verbose output
pytest tests/ -v

Run a specific test
pytest tests/ -k test_add_task

🛠️ 6. Troubleshooting Common Errors
❌ ModuleNotFoundError (e.g. rich not found)
ModuleNotFoundError: No module named 'rich'


Solution:
pip install -r requirements.txt

❌ ImportError (relative import issue)

Cause: Wrong directory or wrong run command
Fix:

Ensure you are inside phase1_console\phase1_todo

Always prefer:
python -m app.cli


❌ pytest not found
'pytest' is not recognized as a command

Solution:
pip install pytest

❌ CLI not opening

Checklist:

✅ Python version 3.13+

✅ Correct directory

✅ UTF-8 terminal enabled (for emojis)

📌 7. Correct Working Directory (IMPORTANT)

Always run commands from:

phase1_console\phase1_todo\

You should see:

app/
tests/
requirements.txt
README.md

⚙️ 8. Environment Setup (Recommended)
Step-by-Step
cd phase1_console\phase1_todo
python -m venv venv


Activate environment:

Windows

venv\Scripts\activate
Linux / macOS

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run app:

bash
Copy code
python -m app.cli
Run tests:

bash
Copy code
pytest tests/ -v
⚡ Quick Reference Card
bash
Copy code
# Setup
cd phase1_console\phase1_todo
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run App
python -m app.cli

# Run Tests
pytest tests/ -v
🎯 Task Priorities
Emoji	Priority	Usage
🔴	High	Urgent / critical tasks
🟡	Medium	Default priority
🟢	Low	Optional / flexible tasks

📌 Task Status
Symbol	Meaning
✅	Completed
⏳	Pending
⚠️	Overdue

