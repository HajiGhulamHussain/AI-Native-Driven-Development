# AI-Native Advanced Todo Console App

Phase 1 implementation for Governor House GIAIC Hackathon 2 - A colorful, interactive CLI-based todo application with full spec-driven development.

## Features

- ➕ **Add Task** - Create tasks with title, description, priority, and due date
- ❌ **Delete Task** - Remove tasks with confirmation prompt
- ✏️ **Update Task** - Modify task attributes (title, description, priority, due date)
- 📋 **View Tasks** - Display all tasks with color-coding, emojis, and sorting
- ✅ **Mark Complete** - Toggle task completion status
- 🔍 **Search Tasks** - Find tasks by keyword, priority, or status
- 📊 **Task Summary** - Show statistics (total, completed, pending, overdue)
- 🟢 🟡 🔴 **Priority Highlight** - Color-code tasks by priority
- 🚪 **Interactive Menu** - Easy-to-use emoji-enhanced navigation

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Terminal with UTF-8 support

### Setup

```bash
cd phase1_todo
pip install -r requirements.txt
```

Or with virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

### Start the Application

```bash
python -m app.cli
```

Or directly:

```bash
python app/cli.py
```

### Main Menu

```
═════════════════════════════════════════════════
      📋 AI-Native Advanced Todo Console App
═════════════════════════════════════════════════

[1] ➕ Add Task
[2] ❌ Delete Task
[3] ✏️ Update Task
[4] 📋 View Tasks
[5] ✅ Mark Complete
[6] 🔍 Search Tasks
[7] 📊 Task Summary
[0] 🚪 Exit

═════════════════════════════════════════════════
Your choice: _
```

### Task Priorities

- 🔴 **High** - Urgent tasks, critical deadlines
- 🟡 **Medium** - Normal priority (default)
- 🟢 **Low** - Optional tasks, can wait

### Task Status

- ✅ **Completed** - Task is done
- ⏳ **Pending** - Task in progress or not started
- ⚠️ **Overdue** - Pending task past its due date

### Example Workflow

1. **Add a task**: Select `[1]`, enter title "Buy groceries", skip optional fields
2. **View tasks**: Select `[4]`, choose sort by priority
3. **Mark complete**: Select `[5]`, enter task ID
4. **Delete task**: Select `[2]`, enter task ID, confirm with `y`
5. **View summary**: Select `[7]` to see statistics
6. **Exit**: Select `[0]` to quit (note: in-memory tasks are lost)

## Features Details

### Add Task

Add new tasks with:
- **Title** (required): Max 200 characters
- **Description** (optional): Additional details
- **Priority** (optional): High/Medium/Low (defaults to Medium)
- **Due Date** (optional): Format YYYY-MM-DD, must be today or future

### View Tasks

Display all tasks with sorting options:
- **By Priority** (default): High > Medium > Low
- **By Due Date**: Soonest due date first
- **By Creation Date**: Newest tasks first

### Search Tasks

Find tasks by:
- **Keyword**: Searches title and description (case-insensitive)
- **Priority**: Filter by High/Medium/Low
- **Status**: Filter by completed/pending

### Task Summary

Statistics showing:
- Total tasks
- Completed count (with percentage)
- Pending count (with percentage)
- Overdue count (percentage of pending tasks)
- Priority breakdown (High/Medium/Low counts)

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

## Specifications

- **Constitution**: `.specify/memory/constitution.md` - Project principles and governance
- **Feature Spec**: `specs/1-console-todo-cli/spec.md` - Complete feature specification
- **Implementation Plan**: `specs/1-console-todo-cli/plan.md` - Architecture and technical decisions
- **Data Model**: `specs/1-console-todo-cli/data-model.md` - Task entity definition
- **CLI Contracts**: `specs/1-console-todo-cli/contracts/cli-interface.md` - Input/output specifications
- **Quick Start**: `specs/1-console-todo-cli/quickstart.md` - Getting started guide

## Development

### AI-Native Development

This project follows AI-native, spec-driven development methodology:

1. **Specification First**: All features are specified before implementation
2. **Test-First Development**: Tests written before implementation (Red-Green-Refactor)
3. **AI-Generated Code**: All code is generated by Claude Code from specifications
4. **No Manual Coding**: Manual coding is strictly prohibited

### Test-First Development

Follow the Red-Green-Refactor cycle:

1. **Red**: Write failing test
2. **Green**: Implement code to make test pass
3. **Refactor**: Improve code without breaking tests

### Constitution Principles

1. **AI-Native Development**: Code generated through Claude Code only
2. **Spec-Driven Development**: Every feature has complete specification
3. **Modular Design**: Independent, testable modules
4. **CLI UX Excellence**: Colors, emojis, interactive menus
5. **Input Validation**: All inputs validated, graceful error recovery
6. **AI Agent Foundation**: Ready for Phase 2+ AI integration

## Limitations (Phase 1)

- **No Persistent Storage**: Tasks are lost when app exits (in-memory only)
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

## Dependencies

- **rich>=13.0.0** - For colored terminal output and emojis
- **pytest>=7.0.0** - For automated testing

## License

This is a hackathon project for Governor House GIAIC Hackathon 2 - Phase 1.

## Contributing

This project follows strict AI-native development:
1. All code must be generated from specifications
2. Manual coding is prohibited
3. All changes must include corresponding tests
4. Constitution principles must be followed

## Support

- **Issue Tracker**: [Add issue here]
- **Specifications**: `specs/1-console-todo-cli/`
- **Constitution**: `.specify/memory/constitution.md`

---

**Happy Task Management! 🎉**
