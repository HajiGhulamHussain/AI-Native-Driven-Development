# CLI Interface Contracts

**Date**: 2026-01-05
**Feature**: 1-console-todo-cli
**Purpose**: Define CLI input/output specifications for all user interactions

## Overview

This document defines the contracts for all CLI interactions, including menu options, input prompts, output formats, and error messages. These contracts serve as the interface between `cli.py` and the underlying task operations in `tasks.py`.

## Main Menu Contract

### Display Format

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

### Input Specifications

| Option | Command | Feature | Priority |
|--------|---------|---------|----------|
| 0 | Exit | Exit application | P1 |
| 1 | Add Task | Create new task | P1 |
| 2 | Delete Task | Remove task | P2 |
| 3 | Update Task | Modify task | P2 |
| 4 | View Tasks | Display all tasks | P1 |
| 5 | Mark Complete | Toggle status | P1 |
| 6 | Search Tasks | Find tasks | P2 |
| 7 | Task Summary | Show statistics | P2 |

### Validation Rules

- Input must be a single digit (0-7)
- Invalid input: Display error "⚠️ Invalid choice. Please enter a number between 0 and 7."
- Return to menu after any action completes
- Clear screen before redisplaying menu (optional)

---

## Feature 1: Add Task Contract

### Prompt Sequence

```
[1] ➕ Add Task
───────────────────────────────────────────────────
Enter task title: _
```

**If title is empty**:
```
⚠️ Title is required.
Press Enter to continue...
```

**If title > 200 chars**:
```
⚠️ Title cannot exceed 200 characters.
Press Enter to continue...
```

**After valid title**:
```
Enter task description (optional, press Enter to skip): _
```

**After description**:
```
Enter priority (High/Medium/Low, default Medium): _
```

**If invalid priority**:
```
⚠️ Invalid priority. Must be High, Medium, or Low.
Using default: Medium.
```

**After priority**:
```
Enter due date (YYYY-MM-DD, optional, press Enter to skip): _
```

**If invalid date format**:
```
⚠️ Invalid date format. Use YYYY-MM-DD.
Press Enter to continue...
```

**If past date**:
```
⚠️ Due date cannot be in the past.
Press Enter to continue...
```

**Success Output**:
```
✅ Task added successfully!
Press Enter to continue...
```

### Input Validation

| Field | Required | Validation | Default | Error Message |
|-------|----------|------------|---------|---------------|
| Title | Yes | Non-empty, max 200 chars | None | "Title is required" or "Title cannot exceed 200 characters" |
| Description | No | None | None | N/A |
| Priority | No | High/Medium/Low (case-insensitive) | Medium | "Invalid priority. Must be High, Medium, or Low" |
| Due Date | No | YYYY-MM-DD format, not past | None | "Invalid date format. Use YYYY-MM-DD" or "Due date cannot be in the past" |

---

## Feature 2: Delete Task Contract

### Prompt Sequence

```
[2] ❌ Delete Task
───────────────────────────────────────────────────
Enter task ID to delete: _
```

**If invalid task ID**:
```
⚠️ Task not found. Invalid task ID.
Press Enter to continue...
```

**If valid task ID**:
```
Are you sure you want to delete "[Task Title]"? (y/n): _
```

**If confirmation is 'y' or 'yes'**:
```
✅ Task deleted successfully!
Press Enter to continue...
```

**If confirmation is 'n' or 'no'**:
```
Task not deleted.
Press Enter to continue...
```

**If no tasks exist**:
```
No tasks available to delete.
Press Enter to continue...
```

### Validation Rules

- Task ID must be a positive integer
- Task must exist in current task list
- Confirmation is case-insensitive (y/yes/n/no)
- Confirmation required before deletion

---

## Feature 3: Update Task Contract

### Prompt Sequence

```
[3] ✏️ Update Task
───────────────────────────────────────────────────
Enter task ID to update: _
```

**If invalid task ID**:
```
⚠️ Task not found. Invalid task ID.
Press Enter to continue...
```

**If no tasks exist**:
```
No tasks available to update.
Press Enter to continue...
```

**If valid task ID**:
```
Select field to update:
[1] Title
[2] Description
[3] Priority
[4] Due Date
[0] Cancel

Your choice: _
```

**If user selects Title (1)**:
```
Enter new title: _
```
- Same validation as Add Task
- Success: "✅ Title updated!"

**If user selects Description (2)**:
```
Enter new description (press Enter to clear): _
```
- No validation required
- Success: "✅ Description updated!"

**If user selects Priority (3)**:
```
Enter new priority (High/Medium/Low): _
```
- Same validation as Add Task
- Success: "✅ Priority updated!"

**If user selects Due Date (4)**:
```
Enter new due date (YYYY-MM-DD, press Enter to clear): _
```
- Same validation as Add Task
- Success: "✅ Due date updated!"

**If user selects Cancel (0)**:
```
Update cancelled.
Press Enter to continue...
```

**If invalid field choice**:
```
⚠️ Invalid choice. Please enter a number between 0 and 4.
Press Enter to continue...
```

---

## Feature 4: View Tasks Contract

### Prompt Sequence

```
[4] 📋 View Tasks
───────────────────────────────────────────────────

Sort by:
[1] Priority (default)
[2] Due Date
[3] Creation Date

Your choice (1-3): _
```

**If no tasks exist**:
```
📋 No tasks yet. Use [1] to add your first task!
Press Enter to continue...
```

**If tasks exist, sorted by Priority**:
```
📋 All Tasks (sorted by priority)
═══════════════════════════════════════════════════

[1] 🔴 HIGH      ✅ Buy groceries
    Created: 2026-01-05 10:30
    Priority: High | Status: Completed

[2] 🟡 MEDIUM    ⏳ Prepare hackathon demo
    Due: 2026-01-10
    Created: 2026-01-05 11:00
    Priority: Medium | Status: Pending

[3] 🟢 LOW       ⏳ Submit proposal
    Due: 2026-01-01 ⚠️ OVERDUE
    Created: 2026-01-03 09:00
    Priority: Low | Status: Pending

═══════════════════════════════════════════════════
Total: 3 tasks
Press Enter to continue...
```

**Sorted by Due Date**:
```
📋 All Tasks (sorted by due date)
═══════════════════════════════════════════════════

[1] ⚠️ Submit proposal
    Due: 2026-01-01 (OVERDUE)
    Priority: Low | Status: Pending

[2] Buy groceries
    Priority: High | Status: Completed

[3] Prepare hackathon demo
    Due: 2026-01-10
    Priority: Medium | Status: Pending

═══════════════════════════════════════════════════
Total: 3 tasks
Press Enter to continue...
```

**Sorted by Creation Date**:
```
📋 All Tasks (sorted by creation date)
═══════════════════════════════════════════════════

[1] Prepare hackathon demo
    Created: 2026-01-05 11:00 (NEWEST)
    Priority: Medium | Status: Pending

[2] Buy groceries
    Created: 2026-01-05 10:30
    Priority: High | Status: Completed

[3] Submit proposal
    Created: 2026-01-03 09:00 (OLDEST)
    Priority: Low | Status: Pending

═══════════════════════════════════════════════════
Total: 3 tasks
Press Enter to continue...
```

### Display Rules

- Tasks are numbered (starting from 1)
- Priority emoji and color always shown
- Status emoji shown: ✅ Completed, ⏳ Pending
- Overdue indicator ⚠️ shown for pending tasks with past due dates
- Description shown only if non-empty (on separate line)
- Creation date shown in format: YYYY-MM-DD HH:MM
- Due date shown if set (overdue tasks highlighted)
- Empty state: friendly message encouraging user to add tasks

---

## Feature 5: Mark Complete Contract

### Prompt Sequence

```
[5] ✅ Mark Complete
───────────────────────────────────────────────────
Enter task ID to toggle: _
```

**If no tasks exist**:
```
No tasks available. Add tasks first using [1] Add Task.
Press Enter to continue...
```

**If invalid task ID**:
```
⚠️ Invalid task number. Please enter a valid task ID.
Press Enter to continue...
```

**If task is marked as pending → completed**:
```
✅ Task marked as completed!
Press Enter to continue...
```

**If task is marked as completed → pending**:
```
⏳ Task marked as pending.
Press Enter to continue...
```

### Behavior

- Toggle status between PENDING and COMPLETED
- No confirmation required (user can toggle back if needed)
- Visual feedback via emoji in success message

---

## Feature 6: Search Tasks Contract

### Prompt Sequence

```
[6] 🔍 Search Tasks
───────────────────────────────────────────────────

Search by:
[1] Keyword
[2] Priority
[3] Status

Your choice (1-3): _
```

**If no tasks exist**:
```
No tasks available to search.
Press Enter to continue...
```

**If user selects Keyword (1)**:
```
Enter keyword to search: _
```

**If user selects Priority (2)**:
```
Enter priority (High/Medium/Low): _
```

**If user selects Status (3)**:
```
Enter status (completed/pending): _
```

**If no matches found**:
```
🔍 No tasks found matching "[search term]".
Try a different search.
Press Enter to continue...
```

**If matches found**:
```
🔍 Search Results: "demo"
═══════════════════════════════════════════════════

[1] Prepare hackathon demo
    Due: 2026-01-10
    Created: 2026-01-05 11:00
    Priority: Medium | Status: Pending

═══════════════════════════════════════════════════
Found 1 task(s) matching "demo"
Press Enter to continue...
```

**Keyword matching**:
- Case-insensitive search in title and description
- Highlight matching term (bold or different color)

**Priority matching**:
- Case-insensitive exact match
- Show all tasks with matching priority

**Status matching**:
- Case-insensitive exact match
- Show all tasks with matching status

---

## Feature 7: Task Summary Contract

### Display Format

```
[7] 📊 Task Summary
───────────────────────────────────────────────────

📊 Task Summary
═══════════════════════════════════════════════════

Total Tasks:        3
✅ Completed:       1 (33%)
⏳ Pending:         2 (67%)
⚠️ Overdue:         1 (33% of pending)

Priority Breakdown:
🔴 High:            1 (33%)
🟡 Medium:          1 (33%)
🟢 Low:             1 (33%)

═══════════════════════════════════════════════════
Press Enter to continue...
```

**If no tasks exist**:
```
📊 Task Summary: Total: 0 | ✅ Completed: 0 | ⏳ Pending: 0 | ⚠️ Overdue: 0
Press Enter to continue...
```

**If all tasks completed**:
```
📊 Task Summary: Total: 5 | ✅ Completed: 5 (100%) | ⏳ Pending: 0 | ⚠️ Overdue: 0
🎉 All tasks completed!
Press Enter to continue...
```

### Statistics Calculation

- Total: Count of all tasks
- Completed: Tasks with status COMPLETED
- Pending: Tasks with status PENDING
- Overdue: Pending tasks with due_date < today
- Percentages: Calculated relative to total tasks
- Priority breakdown: Count of tasks per priority level

---

## Feature 9: Exit Contract

### Prompt Sequence

```
[0] 🚪 Exit
───────────────────────────────────────────────────

Goodbye! 👋

Task Session Summary:
─────────────────────
Total Tasks: 3
Completed: 1
Pending: 2

💾 Note: Tasks are saved in-memory and will be lost when the app exits.
   Enable persistence in Phase 2 for permanent storage.

═══════════════════════════════════════════════════
```

**Application terminates**

### Exit Behavior

- Display goodbye message
- Show session summary (optional but recommended)
- Note about in-memory storage limitation
- Clean exit (no error messages)
- Application process terminates

---

## Error Messages Contract

### Common Error Patterns

| Error Type | Message Format | Color | Emoji |
|------------|----------------|-------|-------|
| Input validation | `⚠️ {specific_error_message}` | Red | ⚠️ |
| Task not found | `⚠️ Task not found. Invalid task ID.` | Red | ⚠️ |
| Invalid choice | `⚠️ Invalid choice. Please enter a number between {min} and {max}.` | Red | ⚠️ |
| No tasks | `No tasks available. {action_suggestion}` | Yellow | ⚠️ (or no emoji) |
| Success | `✅ {action} successfully!` | Green | ✅ |
| Cancelled | `{action} cancelled.` | Yellow | (no emoji) |

### Error Message Examples

```
⚠️ Title cannot be empty.
⚠️ Title cannot exceed 200 characters.
⚠️ Invalid priority. Must be High, Medium, or Low.
⚠️ Invalid date format. Use YYYY-MM-DD.
⚠️ Due date cannot be in the past.
⚠️ Task not found. Invalid task ID.
⚠️ Invalid choice. Please enter a number between 0 and 7.
✅ Task added successfully!
✅ Task deleted successfully!
✅ Task updated successfully!
✅ Task marked as completed!
```

### Graceful Error Recovery

1. Display error message in red with ⚠️
2. Wait for user to press Enter
3. Return to main menu
4. Do not crash application
5. Preserve task data

---

## Colors and Styling Contract

### Color Scheme (via Rich Library)

| Element | Color | Purpose |
|---------|-------|---------|
| Success messages | Green | Confirmation of successful actions |
| Error messages | Red | Validation errors, invalid inputs |
| Warning messages | Yellow | Non-critical issues, cancellations |
| High priority tasks | Red | Visual indicator for importance |
| Medium priority tasks | Yellow | Visual indicator for importance |
| Low priority tasks | Green | Visual indicator for importance |
| Headers/Dividers | Cyan or Blue | Visual separation |
| Task numbers | Bright | Easy identification |
| Metadata (dates) | Dim or Gray | Secondary information |

### Emoji Usage

| Emoji | Purpose |
|-------|---------|
| ➕ | Add Task |
| ❌ | Delete Task |
| ✏️ | Update Task |
| 📋 | View Tasks |
| ✅ | Completed status |
| ⏳ | Pending status |
| ⚠️ | Overdue or errors |
| 🔴 | High priority |
| 🟡 | Medium priority |
| 🟢 | Low priority |
| 🔍 | Search |
| 📊 | Summary/Statistics |
| 🚪 | Exit |
| 👋 | Goodbye |
| 🎉 | Celebration (all tasks completed) |

---

## Unicode Support

### Requirements

- All text must support UTF-8 encoding
- Emojis must display correctly in supported terminals
- Graceful degradation for terminals without emoji support
- Handle Unicode characters in task titles/descriptions

### Implementation Notes

- Python 3.11+ defaults to UTF-8 for string handling
- Rich library automatically detects terminal capabilities
- Emojis will not break on terminals that don't support them
- Consider fallback text for emoji-only displays (optional)

---

## References

- Feature Specification: `specs/1-console-todo-cli/spec.md`
- Data Model: `specs/1-console-todo-cli/data-model.md`
- Constitution: `.specify/memory/constitution.md`
- Functional Requirements: FR-001 through FR-025
- Constitution Principle IV: CLI UX Excellence (colors and emojis)
- Constitution Principle V: Input Validation & Error Handling
