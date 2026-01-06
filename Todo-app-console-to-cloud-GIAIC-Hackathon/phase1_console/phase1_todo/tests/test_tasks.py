"""
Unit and integration tests for AI-Native Advanced Todo Console App.

Follows testing requirements from constitution and functional requirements from spec.
Test-First Development: Red-Green-Refactor cycle.
"""

import pytest
from datetime import date, datetime, timedelta
from app.tasks import (
    Task,
    Priority,
    Status,
    add_task,
    get_task,
    search_tasks,
    update_task,
    delete_task,
    toggle_status,
    sort_tasks,
    get_summary,
    validate_title,
    validate_priority,
    validate_due_date,
)


# ============================================================================
# Create (Add Task) Tests
# ============================================================================

def test_add_task_minimal():
    """Test adding a task with only title (default values)."""
    tasks: List[Task] = []
    task = add_task(tasks, "Buy groceries")

    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.description is None
    assert task.priority == Priority.MEDIUM
    assert task.due_date is None
    assert task.status == Status.PENDING
    assert len(tasks) == 1


def test_add_task_complete():
    """Test adding a task with all fields."""
    tasks: List[Task] = []
    future_date = date.today() + timedelta(days=7)

    task = add_task(
        tasks,
        title="Prepare presentation",
        description="Create slides and practice",
        priority=Priority.HIGH,
        due_date=future_date
    )

    assert task.id == 1
    assert task.title == "Prepare presentation"
    assert task.description == "Create slides and practice"
    assert task.priority == Priority.HIGH
    assert task.due_date == future_date
    assert task.status == Status.PENDING
    assert len(tasks) == 1


def test_add_task_empty_title():
    """Test adding task with empty title."""
    tasks: List[Task] = []

    with pytest.raises(ValueError, match="Title is required"):
        add_task(tasks, "")


def test_add_task_whitespace_title():
    """Test adding task with whitespace title."""
    tasks: List[Task] = []

    with pytest.raises(ValueError, match="Title is required"):
        add_task(tasks, "   ")


def test_add_task_past_due_date():
    """Test adding task with past due date."""
    tasks: List[Task] = []
    past_date = date.today() - timedelta(days=1)

    with pytest.raises(ValueError, match="Due date cannot be in the past"):
        add_task(tasks, "Test task", due_date=past_date)


def test_add_task_multiple():
    """Test adding multiple tasks."""
    tasks: List[Task] = []

    task1 = add_task(tasks, "First task")
    task2 = add_task(tasks, "Second task")
    task3 = add_task(tasks, "Third task")

    assert len(tasks) == 3
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3


# ============================================================================
# Read (Get Task) Tests
# ============================================================================

def test_get_task_found():
    """Test getting an existing task."""
    tasks: List[Task] = []
    added_task = add_task(tasks, "Test task")
    found_task = get_task(tasks, 1)

    assert found_task is not None
    assert found_task.id == 1
    assert found_task.title == "Test task"


def test_get_task_not_found():
    """Test getting a non-existent task."""
    tasks: List[Task] = []
    add_task(tasks, "Test task")

    found_task = get_task(tasks, 999)

    assert found_task is None


# ============================================================================
# Search Tests
# ============================================================================

def test_search_tasks_by_keyword():
    """Test searching tasks by keyword."""
    tasks: List[Task] = []
    add_task(tasks, "Buy groceries")
    add_task(tasks, "Prepare meeting")
    add_task(tasks, "Buy office supplies")
    add_task(tasks, "Finish report")

    results = search_tasks(tasks, keyword="buy")

    assert len(results) == 2
    assert all("buy" in t.title.lower() for t in results)


def test_search_tasks_by_keyword_in_description():
    """Test searching tasks by keyword in description."""
    tasks: List[Task] = []
    add_task(tasks, "Task 1", description="Grocery shopping")
    add_task(tasks, "Task 2", description="Office work")
    add_task(tasks, "Task 3", description="Meeting preparation")

    results = search_tasks(tasks, keyword="meeting")

    assert len(results) == 1
    assert results[0].description == "Meeting preparation"


def test_search_tasks_by_priority():
    """Test searching tasks by priority."""
    tasks: List[Task] = []
    add_task(tasks, "High task 1", priority=Priority.HIGH)
    add_task(tasks, "High task 2", priority=Priority.HIGH)
    add_task(tasks, "Medium task", priority=Priority.MEDIUM)
    add_task(tasks, "Low task", priority=Priority.LOW)

    results = search_tasks(tasks, priority=Priority.HIGH)

    assert len(results) == 2
    assert all(t.priority == Priority.HIGH for t in results)


def test_search_tasks_by_status():
    """Test searching tasks by status."""
    tasks: List[Task] = []
    task1 = add_task(tasks, "Task 1")
    task2 = add_task(tasks, "Task 2")
    toggle_status(task1)

    results = search_tasks(tasks, status=Status.COMPLETED)

    assert len(results) == 1
    assert results[0].id == 1


def test_search_tasks_no_results():
    """Test search with no matching results."""
    tasks: List[Task] = []
    add_task(tasks, "Buy groceries")
    add_task(tasks, "Prepare meeting")

    results = search_tasks(tasks, keyword="nonexistent")

    assert len(results) == 0


def test_search_tasks_empty_list():
    """Test search with empty task list."""
    tasks: List[Task] = []

    results = search_tasks(tasks, keyword="test")

    assert len(results) == 0


# ============================================================================
# Update Tests
# ============================================================================

def test_update_task_title():
    """Test updating task title."""
    tasks: List[Task] = []
    task = add_task(tasks, "Original title")

    updated = update_task(tasks, 1, title="New title")

    assert updated.title == "New title"
    assert get_task(tasks, 1).title == "New title"


def test_update_task_description():
    """Test updating task description."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task")

    updated = update_task(tasks, 1, description="New description")

    assert updated.description == "New description"


def test_update_task_priority():
    """Test updating task priority."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task", priority=Priority.MEDIUM)

    updated = update_task(tasks, 1, priority=Priority.HIGH)

    assert updated.priority == Priority.HIGH


def test_update_task_due_date():
    """Test updating task due date."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task")
    new_due_date = date.today() + timedelta(days=10)

    updated = update_task(tasks, 1, due_date=new_due_date)

    assert updated.due_date == new_due_date


def test_update_task_not_found():
    """Test updating non-existent task."""
    tasks: List[Task] = []
    add_task(tasks, "Task")

    with pytest.raises(ValueError, match="Task 999 not found"):
        update_task(tasks, 999, title="New title")


def test_update_task_empty_title():
    """Test updating task with empty title."""
    tasks: List[Task] = []
    task = add_task(tasks, "Original title")

    with pytest.raises(ValueError, match="Title is required"):
        update_task(tasks, 1, title="")


def test_update_task_past_due_date():
    """Test updating task with past due date."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task")
    past_date = date.today() - timedelta(days=1)

    with pytest.raises(ValueError, match="Due date cannot be in the past"):
        update_task(tasks, 1, due_date=past_date)


# ============================================================================
# Delete Tests
# ============================================================================

def test_delete_task():
    """Test deleting a task."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task to delete")
    add_task(tasks, "Other task")

    deleted = delete_task(tasks, 1)

    assert deleted.id == 1
    assert len(tasks) == 1
    assert get_task(tasks, 1) is None


def test_delete_task_not_found():
    """Test deleting non-existent task."""
    tasks: List[Task] = []
    add_task(tasks, "Task")

    with pytest.raises(ValueError, match="Task 999 not found"):
        delete_task(tasks, 999)


# ============================================================================
# Toggle Status Tests
# ============================================================================

def test_toggle_status_to_completed():
    """Test toggling task status to completed."""
    tasks: List[Task] = []
    task = add_task(tasks, "Test task")

    assert task.status == Status.PENDING

    new_status = toggle_status(task)

    assert new_status == Status.COMPLETED
    assert task.status == Status.COMPLETED


def test_toggle_status_to_pending():
    """Test toggling task status back to pending."""
    tasks: List[Task] = []
    task = add_task(tasks, "Test task")
    toggle_status(task)  # Mark as completed

    new_status = toggle_status(task)

    assert new_status == Status.PENDING
    assert task.status == Status.PENDING


# ============================================================================
# Sorting Tests
# ============================================================================

def test_sort_tasks_by_priority():
    """Test sorting tasks by priority."""
    tasks: List[Task] = []
    add_task(tasks, "Low task", priority=Priority.LOW)
    add_task(tasks, "High task", priority=Priority.HIGH)
    add_task(tasks, "Medium task", priority=Priority.MEDIUM)
    add_task(tasks, "Another high task", priority=Priority.HIGH)

    sorted_tasks = sort_tasks(tasks, "priority")

    assert sorted_tasks[0].priority == Priority.HIGH
    assert sorted_tasks[1].priority == Priority.HIGH
    assert sorted_tasks[2].priority == Priority.MEDIUM
    assert sorted_tasks[3].priority == Priority.LOW
    assert sorted_tasks[0].id == 2
    assert sorted_tasks[1].id == 4


def test_sort_tasks_by_due_date():
    """Test sorting tasks by due date."""
    tasks: List[Task] = []
    today = date.today()
    add_task(tasks, "Task 1", due_date=today + timedelta(days=3))
    add_task(tasks, "Task 2", due_date=today + timedelta(days=1))
    add_task(tasks, "Task 3", due_date=None)
    add_task(tasks, "Task 4", due_date=today + timedelta(days=2))

    sorted_tasks = sort_tasks(tasks, "due_date")

    assert sorted_tasks[0].due_date == today + timedelta(days=1)
    assert sorted_tasks[1].due_date == today + timedelta(days=2)
    assert sorted_tasks[2].due_date == today + timedelta(days=3)
    assert sorted_tasks[3].due_date is None


def test_sort_tasks_by_created_at():
    """Test sorting tasks by creation date."""
    tasks: List[Task] = []
    add_task(tasks, "Task 1")
    add_task(tasks, "Task 2")
    add_task(tasks, "Task 3")

    sorted_tasks = sort_tasks(tasks, "created_at")

    assert sorted_tasks[0].id == 3
    assert sorted_tasks[1].id == 2
    assert sorted_tasks[2].id == 1


def test_sort_tasks_invalid_method():
    """Test sorting with invalid method."""
    tasks: List[Task] = []
    add_task(tasks, "Task 1")
    add_task(tasks, "Task 2")

    sorted_tasks = sort_tasks(tasks, "invalid")

    # Should return original order
    assert len(sorted_tasks) == 2
    assert sorted_tasks[0].id == 1


def test_sort_tasks_empty_list():
    """Test sorting empty task list."""
    tasks: List[Task] = []

    sorted_tasks = sort_tasks(tasks, "priority")

    assert len(sorted_tasks) == 0


# ============================================================================
# Summary Tests
# ============================================================================

def test_get_summary_all_pending():
    """Test summary with all pending tasks."""
    tasks: List[Task] = []
    add_task(tasks, "Task 1")
    add_task(tasks, "Task 2")
    add_task(tasks, "Task 3")

    summary = get_summary(tasks)

    assert summary["total"] == 3
    assert summary["completed"] == 0
    assert summary["pending"] == 3
    assert summary["overdue"] == 0


def test_get_summary_all_completed():
    """Test summary with all completed tasks."""
    tasks: List[Task] = []
    task1 = add_task(tasks, "Task 1")
    task2 = add_task(tasks, "Task 2")
    toggle_status(task1)
    toggle_status(task2)

    summary = get_summary(tasks)

    assert summary["total"] == 2
    assert summary["completed"] == 2
    assert summary["pending"] == 0
    assert summary["overdue"] == 0


def test_get_summary_mixed():
    """Test summary with mixed task states."""
    tasks: List[Task] = []
    task1 = add_task(tasks, "Task 1")
    task2 = add_task(tasks, "Task 2")
    task3 = add_task(tasks, "Task 3")
    toggle_status(task1)

    summary = get_summary(tasks)

    assert summary["total"] == 3
    assert summary["completed"] == 1
    assert summary["pending"] == 2
    assert summary["overdue"] == 0


def test_get_summary_with_overdue():
    """Test summary with overdue tasks."""
    tasks: List[Task] = []
    # Add a task with past due date BEFORE adding to the list
    # Since add_task validates due dates, we need to create a task directly
    from datetime import timedelta
    past_date = date.today() - timedelta(days=1)

    task1 = Task(
        task_id=1,
        title="Overdue task",
        description=None,
        priority=Priority.HIGH,
        due_date=past_date,
        status=Status.PENDING,
        created_at=datetime.now()
    )
    tasks.append(task1)

    add_task(tasks, "Normal task")
    add_task(tasks, "Completed task")
    toggle_status(get_task(tasks, 3))

    summary = get_summary(tasks)

    assert summary["total"] == 3
    assert summary["completed"] == 1
    assert summary["pending"] == 2
    assert summary["overdue"] == 1


def test_get_summary_empty_list():
    """Test summary with empty task list."""
    tasks: List[Task] = []

    summary = get_summary(tasks)

    assert summary["total"] == 0
    assert summary["completed"] == 0
    assert summary["pending"] == 0
    assert summary["overdue"] == 0


# ============================================================================
# Integration Tests (User Story Workflows)
# ============================================================================

def test_user_story_1_add_task_workflow():
    """Test User Story 1 workflow: Add Task."""
    tasks: List[Task] = []

    # Add task
    task1 = add_task(tasks, "Buy groceries")
    task2 = add_task(tasks, "Prepare presentation", priority=Priority.HIGH)

    assert len(tasks) == 2

    # View tasks (verify they exist)
    assert get_task(tasks, 1) is not None
    assert get_task(tasks, 2) is not None


def test_user_story_2_and_3_view_and_complete_workflow():
    """Test User Stories 2 & 3 workflow: View and Complete."""
    tasks: List[Task] = []
    task1 = add_task(tasks, "Buy groceries")
    task2 = add_task(tasks, "Prepare meeting")

    # View tasks
    assert get_task(tasks, 1) is not None
    assert get_task(tasks, 2) is not None

    # Complete first task
    toggle_status(task1)
    assert task1.status == Status.COMPLETED

    # Delete second task
    delete_task(tasks, 2)
    assert len(tasks) == 1
    assert get_task(tasks, 2) is None

    # Verify summary
    summary = get_summary(tasks)
    assert summary["total"] == 1
    assert summary["completed"] == 1
    assert summary["pending"] == 0


def test_user_story_6_search_workflow():
    """Test User Story 6 workflow: Search Tasks."""
    tasks: List[Task] = []
    add_task(tasks, "Grocery shopping")
    add_task(tasks, "Meeting preparation")
    add_task(tasks, "Grocery list review")

    # Search for "grocery"
    tasks
    results = search_tasks(tasks, keyword="grocery")

    assert len(results) == 2

    # Update first result
    update_task(tasks, results[0].id, title="Updated grocery task")
    updated_task = get_task(tasks, results[0].id)
    assert updated_task.title == "Updated grocery task"


def test_multiple_operations_on_same_task():
    """Test multiple operations on same task."""
    tasks: List[Task] = []

    # Add task
    task = add_task(tasks, "Multi-operation task")
    assert task.id == 1

    # Update task
    update_task(tasks, 1, description="New description")
    assert task.description == "New description"

    # Complete task
    toggle_status(task)
    assert task.status == Status.COMPLETED

    # Delete task
    delete_task(tasks, 1)
    assert len(tasks) == 0


def test_sort_after_additions_and_deletions():
    """Test sorting after multiple additions and deletions."""
    tasks: List[Task] = []

    # Add tasks
    add_task(tasks, "Low priority", priority=Priority.LOW)
    add_task(tasks, "High priority", priority=Priority.HIGH)
    add_task(tasks, "Medium priority", priority=Priority.MEDIUM)

    # Sort and verify order
    sorted_tasks = sort_tasks(tasks, "priority")
    assert sorted_tasks[0].priority == Priority.HIGH

    # Delete high priority task
    delete_task(tasks, 2)

    # Sort again and verify new order
    sorted_tasks = sort_tasks(tasks, "priority")
    assert sorted_tasks[0].priority == Priority.MEDIUM


# ============================================================================
# Edge Case Tests
# ============================================================================

def test_title_with_200_chars():
    """Test title with exactly 200 characters."""
    tasks: List[Task] = []
    title_200_chars = "a" * 200

    task = add_task(tasks, title_200_chars)

    assert task.title == title_200_chars
    assert len(task.title) == 200


def test_title_with_201_chars_fails():
    """Test title with 201 characters fails validation."""
    tasks: List[Task] = []
    title_201_chars = "a" * 201

    with pytest.raises(ValueError, match="Title cannot exceed 200 characters"):
        add_task(tasks, title_201_chars)


def test_unicode_in_title():
    """Test task title with Unicode characters."""
    tasks: List[Task] = []
    unicode_title = "Buy groceries: 🛒🥕🍇"

    task = add_task(tasks, unicode_title)

    assert task.title == unicode_title


def test_unicode_in_description():
    """Test task description with Unicode characters."""
    tasks: List[Task] = []
    unicode_description = "Meeting with team 🎯 about project 🚀"

    task = add_task(tasks, "Task", description=unicode_description)

    assert task.description == unicode_description


def test_due_date_today():
    """Test task with due date of today."""
    tasks: List[Task] = []
    today = date.today()

    task = add_task(tasks, "Today's task", due_date=today)

    assert task.due_date == today
    assert task.is_overdue() is False


def test_task_with_no_due_date():
    """Test task without due date."""
    tasks: List[Task] = []

    task = add_task(tasks, "No due date task")

    assert task.due_date is None
    assert task.is_overdue() is False


def test_clear_description():
    """Test clearing task description."""
    tasks: List[Task] = []
    task = add_task(tasks, "Task", description="Original description")

    update_task(tasks, 1, description="")

    assert task.description is None


def test_case_insensitive_priority_validation():
    """Test priority validation is case-insensitive."""
    assert validate_priority("HIGH") == Priority.HIGH
    assert validate_priority("Medium") == Priority.MEDIUM
    assert validate_priority("lOw") == Priority.LOW


def test_task_ids_sequential_after_deletion():
    """Test task IDs remain sequential after deletion."""
    tasks: List[Task] = []

    task1 = add_task(tasks, "Task 1")
    task2 = add_task(tasks, "Task 2")
    task3 = add_task(tasks, "Task 3")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3

    # Delete middle task
    delete_task(tasks, 2)

    # Add new task - should get ID 4, not 2
    task4 = add_task(tasks, "Task 4")
    assert task4.id == 4
