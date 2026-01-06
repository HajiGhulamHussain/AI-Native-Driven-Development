# Quick Start Guide: AI-Native Advanced Todo Console App

**Date**: 2026-01-05
**Feature**: 1-console-todo-cli
**Purpose**: Get up and running quickly with the todo application

## Prerequisites

- Python 3.11 or higher installed
- pip (Python package manager) installed
- Terminal/Command Prompt with UTF-8 support

## Installation

### 1. Clone or Navigate to Project

```bash
cd path/to/todo-list-hackathon
cd phase1_todo
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt contents**:
```
rich>=13.0.0
pytest>=7.0.0
```

## Running the Application

### Start the CLI

```bash
python -m app.cli
```

Or directly:
```bash
python app/cli.py
```

You should see the main menu:
```
═══════════════════════════════════════════════════
      📋 AI-Native Advanced Todo Console App
═══════════════════════════════════════════════════

[1] ➕ Add Task
[2] ❌ Delete Task
[3] ✏️ Update Task
[4] 📋 View Tasks
[5] ✅ Mark Complete
[6] 🔍 Search Tasks
[7] 📊 Task Summary
[0] 🚪 Exit

═══════════════════════════════════════════════════
Your choice: _
```

## Basic Usage

### Add Your First Task

1. Select `1` (Add Task)
2. Enter task title: "Buy groceries"
3. Enter description (optional): Press Enter to skip
4. Enter priority (High/Medium/Low): Press Enter for default (Medium)
5. Enter due date (YYYY-MM-DD): Press Enter to skip

Result: ✅ Task added successfully!

### View Your Tasks

1. Select `4` (View Tasks)
2. Choose sort order:
   - `1` for Priority (default)
   - `2` for Due Date
   - `3` for Creation Date

Result: See all your tasks with color-coding and emojis!

### Mark a Task Complete

1. Select `5` (Mark Complete)
2. Enter task ID: `1`

Result: ✅ Task marked as completed!

### See Task Summary

1. Select `7` (Task Summary)

Result: See total tasks, completed, pending, and overdue counts!

### Search Tasks

1. Select `6` (Search Tasks)
2. Choose search type:
   - `1` for Keyword
   - `2` for Priority
   - `3` for Status
3. Enter search term

Result: See matching tasks!

### Delete a Task

1. Select `2` (Delete Task)
2. Enter task ID: `2`
3. Confirm: `y`

Result: ✅ Task deleted successfully!

### Update a Task

1. Select `3` (Update Task)
2. Enter task ID: `3`
3. Select field to update:
   - `1` for Title
   - `2` for Description
   - `3` for Priority
   - `4` for Due Date
4. Enter new value

Result: ✅ Task updated successfully!

### Exit the Application

1. Select `0` (Exit)

Result: Goodbye message and app terminates.

## Feature Reference

| # | Feature | Description | Priority |
|---|---------|-------------|----------|
| 1 | Add Task | Create new task with title, description, priority, due date | P1 |
| 2 | Delete Task | Remove task with confirmation | P2 |
| 3 | Update Task | Modify task attributes | P2 |
| 4 | View Tasks | Display all tasks with sorting options | P1 |
| 5 | Mark Complete | Toggle task completion status | P1 |
| 6 | Search Tasks | Find tasks by keyword, priority, or status | P2 |
| 7 | Task Summary | Show statistics and breakdowns | P2 |
| 8 | Priority Highlight | Color-code tasks by priority | P2 |
| 9 | Interactive Menu | Emoji-enhanced navigation | P1 |

## Tips and Tricks

### Keyboard Shortcuts

- Use number keys (0-7) for quick menu selection
- Press Enter to accept defaults and skip optional fields
- Use `Ctrl+C` at any time to exit immediately (interrupt signal)

### Task Priorities

- 🔴 **High**: Urgent tasks, critical deadlines
- 🟡 **Medium**: Normal priority, most tasks
- 🟢 **Low**: Optional tasks, can wait

### Task Status

- ✅ **Completed**: Task is done
- ⏳ **Pending**: Task in progress or not started
- ⚠️ **Overdue**: Pending task past its due date

### Date Format

Always use YYYY-MM-DD format for due dates:
- Correct: `2026-01-10`, `2026-12-31`
- Incorrect: `01/10/2026`, `Jan 10`, `10th Jan`

### Searching

- **Keyword**: Searches title and description (case-insensitive)
- **Priority**: Exact match (high/medium/low, case-insensitive)
- **Status**: Exact match (completed/pending, case-insensitive)

## Project Structure

```
phase1_todo/
├── app/
│   ├── __init__.py       # Package initialization
│   ├── cli.py            # Main CLI interface
│   └── tasks.py          # Task model and operations
├── tests/
│   └── test_tasks.py     # Unit and integration tests
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## Testing

### Run All Tests

```bash
pytest tests/
```

### Run Tests with Verbose Output

```bash
pytest tests/ -v
```

### Run Specific Test

```bash
pytest tests/ -k test_add_task
```

### Test Coverage

```bash
pytest tests/ --cov=app --cov-report=html
```

## Troubleshooting

### Emojis Not Displaying

**Issue**: Emojis appear as squares or question marks.

**Solution**:
- Update your terminal to support UTF-8
- Use a modern terminal (Windows Terminal, iTerm2, etc.)
- Emojis will gracefully degrade if not supported

### Colors Not Showing

**Issue**: Output is plain text without colors.

**Solution**:
- Ensure your terminal supports ANSI color codes
- Check that Rich library is installed: `pip list | grep rich`
- Some CI/CD environments disable colors automatically

### Import Errors

**Issue**: `ModuleNotFoundError` when running the app.

**Solution**:
- Ensure you're in the `phase1_todo` directory
- Activate your virtual environment
- Install dependencies: `pip install -r requirements.txt`

### Task Data Lost on Restart

**Issue**: Tasks disappear when you restart the app.

**Note**: This is expected behavior for Phase 1. Tasks are stored in-memory and are lost when the app exits. Persistent storage (JSON/database) will be added in Phase 2+.

## Development

### AI-Native Development

This project follows AI-native, spec-driven development methodology:

1. **Specification First**: All features are specified in `specs/1-console-todo-cli/spec.md`
2. **Test-First**: Tests must be written before implementation (Red-Green-Refactor)
3. **AI-Generated Code**: All code is generated by Claude Code from specifications
4. **No Manual Coding**: Manual coding is strictly prohibited

### Constitution

This project follows the constitution defined in `.specify/memory/constitution.md`:

- **AI-Native Development**: Code generated through Claude Code only
- **Spec-Driven Development**: Every feature has complete specification
- **Modular Design**: Independent, testable modules
- **CLI UX Excellence**: Colors, emojis, interactive menus
- **Input Validation**: All inputs validated, graceful error recovery
- **AI Agent Foundation**: Ready for Phase 2+ AI integration

### Testing Requirements

- **pytest** for automated testing
- Each feature must have at least one test
- CLI interactions simulated in tests
- Test-First Development (NON-NEGOTIABLE)

## Limitations (Phase 1)

- **No Persistent Storage**: Tasks are lost when app exits
- **Single User**: No multi-user support or authentication
- **No Categories/Tags**: Task organization limited to priority
- **No Subtasks**: Nested tasks not supported
- **No Task Dependencies**: Tasks are independent
- **No Recurring Tasks**: Cannot create recurring tasks
- **No AI Integration**: Natural language commands coming in Phase 2+

## Future Enhancements (Phase 2+)

- Persistent storage (JSON, SQLite, PostgreSQL)
- Task categories and tags
- Subtasks and task dependencies
- Recurring tasks
- AI agent integration (recommendations, auto-prioritization)
- Natural language commands ("Reschedule my high priority tasks")
- Multi-user support and authentication
- Export/import functionality
- Cloud synchronization

## Support

- **Specification**: `specs/1-console-todo-cli/spec.md`
- **Implementation Plan**: `specs/1-console-todo-cli/plan.md`
- **Data Model**: `specs/1-console-todo-cli/data-model.md`
- **CLI Contracts**: `specs/1-console-todo-cli/contracts/cli-interface.md`
- **Constitution**: `.specify/memory/constitution.md`

## License

This is a hackathon project for Governor House GIAIC Hackathon 2 - Phase 1.

---

**Happy Task Management! 🎉**
