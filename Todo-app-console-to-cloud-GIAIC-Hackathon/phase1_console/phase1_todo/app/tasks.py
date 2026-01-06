from datetime import date, datetime
from enum import Enum
from typing import Optional, List


class Priority(Enum):
    """Task priority levels with color coding and emojis."""
    HIGH = "High"      # 🔴 Red
    MEDIUM = "Medium"  # 🟡 Yellow
    LOW = "Low"        # 🟢 Green


class Status(Enum):
    """Task completion status."""
    PENDING = "pending"   # ⏳
    COMPLETED = "completed"  # ✅


class Task:
    """Represents a todo item with all attributes required by specification."""

    def __init__(
        self,
        task_id: int,
        title: str,
        description: Optional[str] = None,
        priority: Priority = Priority.MEDIUM,
        due_date: Optional[date] = None,
        status: Status = Status.PENDING,
        created_at: Optional[datetime] = None
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.created_at = created_at if created_at else datetime.now()

    def is_overdue(self) -> bool:
        """Check if task is overdue (pending with past due date)."""
        return (
            self.status == Status.PENDING and
            self.due_date is not None and
            self.due_date < date.today()
        )

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}', priority={self.priority.value}, status={self.status.value})"


def validate_title(title: str) -> None:
    """
    Validate task title.

    Raises:
        ValueError: If title is empty or exceeds 200 characters

    Args:
        title: Task title to validate
    """
    if not title or not title.strip():
        raise ValueError("Title is required")
    if len(title) > 200:
        raise ValueError("Title cannot exceed 200 characters")


def validate_priority(priority_str: str) -> Priority:
    """
    Validate and parse priority string.

    Args:
        priority_str: Priority string (case-insensitive)

    Returns:
        Priority enum value

    Raises:
        ValueError: If priority is invalid
    """
    try:
        return Priority[priority_str.strip().upper()]
    except KeyError:
        raise ValueError("Invalid priority. Must be High, Medium, or Low")


def validate_due_date(date_str: str) -> Optional[date]:
    """
    Validate and parse due date string.

    Args:
        date_str: Due date string in YYYY-MM-DD format

    Returns:
        Date object if valid, None if empty

    Raises:
        ValueError: If date format is invalid or date is in the past
    """
    if not date_str or not date_str.strip():
        return None

    try:
        due_date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    if due_date < date.today():
        raise ValueError("Due date cannot be in the past")

    return due_date


def add_task(
    tasks: List[Task],
    title: str,
    description: Optional[str] = None,
    priority: Priority = Priority.MEDIUM,
    due_date: Optional[date] = None
) -> Task:
    """
    Create and add new task. Validates all inputs.

    Args:
        tasks: List of existing tasks
        title: Task title (required)
        description: Optional task description
        priority: Task priority (defaults to Medium)
        due_date: Optional due date

    Returns:
        Created Task object

    Raises:
        ValueError: If validation fails
    """
    # Validate title
    validate_title(title)

    # Validate due date
    if due_date and due_date < date.today():
        raise ValueError("Due date cannot be in the past")

    # Create task
    new_id = len(tasks) + 1 if tasks else 1
    task = Task(
        task_id=new_id,
        title=title.strip(),
        description=description.strip() if description else None,
        priority=priority,
        due_date=due_date,
        status=Status.PENDING,
        created_at=datetime.now()
    )

    tasks.append(task)
    return task


def get_task(tasks: List[Task], task_id: int) -> Optional[Task]:
    """
    Get task by ID.

    Args:
        tasks: List of tasks
        task_id: Task ID to find

    Returns:
        Task object if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def search_tasks(
    tasks: List[Task],
    keyword: Optional[str] = None,
    priority: Optional[Priority] = None,
    status: Optional[Status] = None
) -> List[Task]:
    """
    Search tasks by keyword, priority, or status.

    Args:
        tasks: List of tasks to search
        keyword: Keyword to search in title and description
        priority: Priority filter
        status: Status filter

    Returns:
        List of matching tasks
    """
    results = tasks.copy()

    if keyword:
        keyword_lower = keyword.lower()
        results = [
            t for t in results
            if keyword_lower in t.title.lower() or
            (t.description and keyword_lower in t.description.lower())
        ]

    if priority:
        results = [t for t in results if t.priority == priority]

    if status:
        results = [t for t in results if t.status == status]

    return results


def update_task(
    tasks: List[Task],
    task_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    priority: Optional[Priority] = None,
    due_date: Optional[date] = None
) -> Task:
    """
    Update task attributes. Validates inputs.

    Args:
        tasks: List of tasks
        task_id: Task ID to update
        title: New title (optional)
        description: New description (optional)
        priority: New priority (optional)
        due_date: New due date (optional)

    Returns:
        Updated Task object

    Raises:
        ValueError: If task not found or validation fails
    """
    task = get_task(tasks, task_id)
    if not task:
        raise ValueError(f"Task {task_id} not found")

    # Validate and update title
    if title is not None:
        validate_title(title)
        task.title = title.strip()

    # Update description
    if description is not None:
        task.description = description.strip() if description.strip() else None

    # Update priority
    if priority is not None:
        task.priority = priority

    # Validate and update due date
    if due_date is not None:
        if due_date and due_date < date.today():
            raise ValueError("Due date cannot be in the past")
        task.due_date = due_date

    return task


def delete_task(tasks: List[Task], task_id: int) -> Task:
    """
    Delete task by ID.

    Args:
        tasks: List of tasks
        task_id: Task ID to delete

    Returns:
        Deleted Task object

    Raises:
        ValueError: If task not found
    """
    task = get_task(tasks, task_id)
    if not task:
        raise ValueError(f"Task {task_id} not found")

    tasks.remove(task)
    return task


def toggle_status(task: Task) -> Status:
    """
    Toggle task status between PENDING and COMPLETED.

    Args:
        task: Task to toggle status

    Returns:
        New status value
    """
    if task.status == Status.PENDING:
        task.status = Status.COMPLETED
    else:
        task.status = Status.PENDING
    return task.status


def sort_tasks(tasks: List[Task], by: str = "priority") -> List[Task]:
    """
    Sort tasks by priority, due date, or creation date.

    Args:
        tasks: List of tasks to sort
        by: Sort method ("priority", "due_date", or "created_at")

    Returns:
        Sorted list of tasks
    """
    priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}

    if by == "priority":
        return sorted(tasks, key=lambda t: (priority_order[t.priority], t.id))
    elif by == "due_date":
        return sorted(
            tasks,
            key=lambda t: (t.due_date if t.due_date else date.max, t.id)
        )
    elif by == "created_at":
        return sorted(tasks, key=lambda t: t.created_at, reverse=True)
    else:
        return tasks


def get_summary(tasks: List[Task]) -> dict:
    """
    Calculate task summary statistics.

    Args:
        tasks: List of tasks

    Returns:
        Dictionary with total, completed, pending, and overdue counts
    """
    total = len(tasks)
    completed = sum(1 for t in tasks if t.status == Status.COMPLETED)
    pending = total - completed
    overdue = sum(1 for t in tasks if t.is_overdue())

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue
    }
