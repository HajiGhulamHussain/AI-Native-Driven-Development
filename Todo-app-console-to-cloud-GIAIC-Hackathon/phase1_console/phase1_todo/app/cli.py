from typing import List, Optional
from rich.console import Console
from rich.text import Text
from datetime import date
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

# Initialize Rich console
console = Console()

# Display styles
SUCCESS_STYLE = "green"
ERROR_STYLE = "red"
WARNING_STYLE = "yellow"
HEADER_STYLE = "bright_cyan"


def print_error(message: str) -> None:
    """Print error message with warning in red."""
    console.print(Text(f"WARNING {message}"), style=ERROR_STYLE)


def print_success(message: str) -> None:
    """Print success message with checkmark in green."""
    console.print(Text(f"SUCCESS {message}"), style=SUCCESS_STYLE)


def print_warning(message: str) -> None:
    """Print warning message in yellow."""
    console.print(Text(message), style=WARNING_STYLE)


def print_header(text: str) -> None:
    """Print header with double line borders."""
    line = "=" * 60
    console.print(line, style=HEADER_STYLE)
    console.print(f"      {text}", style=HEADER_STYLE)
    console.print(line, style=HEADER_STYLE)


def wait_for_enter() -> None:
    """Wait for user to press Enter."""
    console.input("Press Enter to continue...")


def display_menu(tasks: List[Task]) -> None:
    """Display main interactive menu."""
    console.clear()
    print_header("AI-Native Advanced Todo Console App")
    console.print()
    console.print("[1] Add Task")
    console.print("[2] Delete Task")
    console.print("[3] Update Task")
    console.print("[4] View Tasks")
    console.print("[5] Mark Complete")
    console.print("[6] Search Tasks")
    console.print("[7] Task Summary")
    console.print("[0] Exit")
    console.print()
    console.print("=" * 60, style=HEADER_STYLE)


def get_menu_choice() -> Optional[int]:
    """Get and validate menu choice from user."""
    try:
        choice = console.input("Your choice: ").strip()
        if not choice:
            return None
        return int(choice)
    except ValueError:
        return None


def get_task_input(prompt: str, allow_empty: bool = False) -> str:
    """Get task input from user."""
    while True:
        value = console.input(prompt).strip()
        if allow_empty or value:
            return value
        print_error("This field cannot be empty. Please try again.")


def get_sort_choice() -> str:
    """Get sort choice from user."""
    console.print()
    console.print("Sort by:")
    console.print("[1] Priority (default)")
    console.print("[2] Due Date")
    console.print("[3] Creation Date")
    console.print()

    while True:
        choice = console.input("Your choice (1-3): ").strip()
        if not choice or choice == "1":
            return "priority"
        elif choice == "2":
            return "due_date"
        elif choice == "3":
            return "created_at"
        else:
            print_error("Invalid choice. Please enter a number between 1 and 3.")


def get_priority_input() -> Priority:
    """Get priority input from user with default Medium."""
    while True:
        choice = console.input("Enter priority (High/Medium/Low, default Medium): ").strip()
        if not choice:
            return Priority.MEDIUM
        try:
            return validate_priority(choice)
        except ValueError as e:
            print_error(str(e))


def get_due_date_input() -> Optional[date]:
    """Get due date input from user."""
    while True:
        choice = console.input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ").strip()
        if not choice:
            return None
        try:
            return validate_due_date(choice)
        except ValueError as e:
            print_error(str(e))


def display_task(task: Task, show_number: bool = True) -> None:
    """Display a single task with all attributes."""
    # Determine priority emoji and color
    priority_emoji = {
        Priority.HIGH: "red circle",
        Priority.MEDIUM: "yellow circle",
        Priority.LOW: "green circle",
    }
    priority_color = {
        Priority.HIGH: "red",
        Priority.MEDIUM: "yellow",
        Priority.LOW: "green",
    }

    # Determine status emoji
    if task.status == Status.COMPLETED:
        status_emoji = "checkmark"
    elif task.is_overdue():
        status_emoji = "warning OVERDUE"
    else:
        status_emoji = "hourglass"

    # Format task number
    num_prefix = f"[{task.id}] " if show_number else ""

    # Display task
    console.print(
        f"{num_prefix}{priority_emoji[task.priority]} {task.priority.value.upper():<8}    {status_emoji}",
        style=priority_color[task.priority]
    )

    console.print(f"    {task.title}")

    if task.description:
        console.print(f"    Description: {task.description}")

    console.print(f"    Priority: {task.priority.value} | Status: {task.status.value}")

    if task.due_date:
        due_date_str = task.due_date.strftime("%Y-%m-%d")
        if task.is_overdue():
            due_date_str += f" (OVERDUE)"
        console.print(f"    Due: {due_date_str}")
    else:
        console.print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")

    console.print()


def display_tasks(tasks: List[Task], sort_by: str = "priority") -> None:
    """Display all tasks with sorting."""
    if not tasks:
        console.print()
        console.print("No tasks yet. Use [1] to add your first task!")
        console.print()
        return

    # Sort tasks
    sorted_tasks_list = sort_tasks(tasks, sort_by)

    # Display header
    sort_label = {
        "priority": "sorted by priority",
        "due_date": "sorted by due date",
        "created_at": "sorted by creation date",
    }
    console.print()
    console.print(f"All Tasks ({sort_label.get(sort_by, '')})")
    console.print("=" * 60)

    # Display each task
    for task in sorted_tasks_list:
        display_task(task)

    # Display summary
    console.print("=" * 60)
    console.print(f"Total: {len(tasks)} tasks")
    console.print()


def handle_add_task(tasks: List[Task]) -> None:
    """Handle Add Task feature (User Story 1)."""
    console.print()
    console.print("[1] Add Task")
    console.print("-" * 50)

    try:
        # Get title
        title = get_task_input("Enter task title: ")
        validate_title(title)

        # Get description (optional)
        description = get_task_input(
            "Enter task description (optional, press Enter to skip): ",
            allow_empty=True
        )
        description = description if description else None

        # Get priority (optional, default Medium)
        priority = get_priority_input()

        # Get due date (optional)
        due_date = get_due_date_input()

        # Add task
        task = add_task(tasks, title, description, priority, due_date)
        console.print()
        print_success("Task added successfully!")

    except ValueError as e:
        console.print()
        print_error(str(e))


def handle_delete_task(tasks: List[Task]) -> None:
    """Handle Delete Task feature (User Story 4)."""
    if not tasks:
        console.print()
        console.print("No tasks available to delete.")
        console.print()
        return

    console.print()
    console.print("[2] Delete Task")
    console.print("-" * 50)

    # Get task ID
    task_id_str = console.input("Enter task ID to delete: ").strip()
    try:
        task_id = int(task_id_str)
    except ValueError:
        console.print()
        print_error("Task not found. Invalid task ID.")
        return

    # Find task
    task = get_task(tasks, task_id)
    if not task:
        console.print()
        print_error("Task not found. Invalid task ID.")
        return

    # Confirm deletion
    console.print()
    confirm = console.input(
        f"Are you sure you want to delete '{task.title}'? (y/n): "
    ).strip().lower()

    if confirm in ('y', 'yes'):
        delete_task(tasks, task_id)
        console.print()
        print_success("Task deleted successfully!")
    else:
        console.print()
        console.print("Task not deleted.")


def handle_update_task(tasks: List[Task]) -> None:
    """Handle Update Task feature (User Story 7)."""
    if not tasks:
        console.print()
        console.print("No tasks available to update.")
        console.print()
        return

    console.print()
    console.print("[3] Update Task")
    console.print("-" * 50)

    # Get task ID
    task_id_str = console.input("Enter task ID to update: ").strip()
    try:
        task_id = int(task_id_str)
    except ValueError:
        console.print()
        print_error("Task not found. Invalid task ID.")
        return

    # Find task
    task = get_task(tasks, task_id)
    if not task:
        console.print()
        print_error("Task not found. Invalid task ID.")
        return

    # Show update options
    console.print()
    console.print("Select field to update:")
    console.print("[1] Title")
    console.print("[2] Description")
    console.print("[3] Priority")
    console.print("[4] Due Date")
    console.print("[0] Cancel")
    console.print()

    # Get field choice
    while True:
        choice = console.input("Your choice: ").strip()
        if choice == "0":
            console.print()
            console.print("Update cancelled.")
            return
        elif choice == "1":
            # Update title
            new_title = get_task_input("Enter new title: ")
            try:
                update_task(tasks, task_id, title=new_title)
                console.print()
                print_success("Title updated!")
                return
            except ValueError as e:
                print_error(str(e))

        elif choice == "2":
            # Update description
            new_description = console.input(
                "Enter new description (press Enter to clear): "
            ).strip()
            try:
                update_task(tasks, task_id, description=new_description if new_description else None)
                console.print()
                print_success("Description updated!")
                return
            except ValueError as e:
                print_error(str(e))

        elif choice == "3":
            # Update priority
            new_priority = get_priority_input()
            try:
                update_task(tasks, task_id, priority=new_priority)
                console.print()
                print_success("Priority updated!")
                return
            except ValueError as e:
                print_error(str(e))

        elif choice == "4":
            # Update due date
            new_due_date = get_due_date_input()
            try:
                update_task(tasks, task_id, due_date=new_due_date)
                console.print()
                print_success("Due date updated!")
                return
            except ValueError as e:
                print_error(str(e))

        else:
            print_error("Invalid choice. Please enter a number between 0 and 4.")


def handle_view_tasks(tasks: List[Task]) -> None:
    """Handle View Tasks feature (User Story 2)."""
    console.print()
    console.print("[4] View Tasks")
    console.print("-" * 50)

    # Get sort choice
    sort_by = get_sort_choice()

    # Display tasks
    display_tasks(tasks, sort_by)


def handle_mark_complete(tasks: List[Task]) -> None:
    """Handle Mark Complete feature (User Story 3)."""
    if not tasks:
        console.print()
        console.print("No tasks available. Add tasks first using [1] Add Task.")
        console.print()
        return

    console.print()
    console.print("[5] Mark Complete")
    console.print("-" * 50)

    # Get task ID
    task_id_str = console.input("Enter task ID to toggle: ").strip()
    try:
        task_id = int(task_id_str)
    except ValueError:
        console.print()
        print_error("Invalid task number. Please enter a valid task ID.")
        return

    # Find task
    task = get_task(tasks, task_id)
    if not task:
        console.print()
        print_error("Invalid task number. Please enter a valid task ID.")
        return

    # Toggle status
    new_status = toggle_status(task)
    if new_status == Status.COMPLETED:
        console.print()
        print_success("Task marked as completed!")
    else:
        console.print()
        console.print("Task marked as pending.")


def handle_search_tasks(tasks: List[Task]) -> None:
    """Handle Search Tasks feature (User Story 6)."""
    if not tasks:
        console.print()
        console.print("No tasks available to search.")
        console.print()
        return

    console.print()
    console.print("[6] Search Tasks")
    console.print("-" * 50)

    # Show search options
    console.print()
    console.print("Search by:")
    console.print("[1] Keyword")
    console.print("[2] Priority")
    console.print("[3] Status")

    # Get search type
    keyword = None
    priority_filter = None
    status_filter = None
    search_term = ""

    while True:
        choice = console.input("Your choice (1-3): ").strip()
        if choice == "1":
            search_term = console.input("Enter keyword to search: ").strip()
            if not search_term:
                keyword = None
            else:
                keyword = search_term
            break
        elif choice == "2":
            search_term = console.input("Enter priority (High/Medium/Low): ").strip()
            if not search_term:
                priority_filter = None
            else:
                try:
                    priority_filter = validate_priority(search_term)
                    search_term = priority_filter.value
                except ValueError as e:
                    print_error(str(e))
                    return
            break
        elif choice == "3":
            search_term = console.input("Enter status (completed/pending): ").strip()
            if not search_term:
                status_filter = None
            else:
                try:
                    status_filter = Status[search_term.strip().upper()]
                    search_term = status_filter.value
                except KeyError:
                    print_error("Invalid status. Must be completed or pending.")
                    return
            break
        else:
            print_error("Invalid choice. Please enter a number between 1 and 3.")

    # Search tasks
    results = search_tasks(tasks, keyword, priority_filter, status_filter)

    # Display results
    if not results:
        console.print()
        console.print(f"No tasks found matching '{search_term}'.")
        console.print("Try a different search.")
        console.print()
    else:
        console.print()
        console.print(f"Search Results: '{search_term}'")
        console.print("=" * 60)
        for task in results:
            display_task(task)
        console.print("=" * 60)
        console.print(f"Found {len(results)} task(s) matching '{search_term}'")
        console.print()


def handle_task_summary(tasks: List[Task]) -> None:
    """Handle Task Summary feature (User Story 5)."""
    console.print()
    console.print("[7] Task Summary")
    console.print("-" * 50)

    # Get summary
    summary = get_summary(tasks)

    # Display summary
    console.print()
    console.print("Task Summary")
    console.print("=" * 60)
    console.print(f"Total Tasks:        {summary['total']:>15} | {summary['total']}")
    console.print(f"checkmark Completed:       {summary['completed']:>15} | ({summary['completed']}/{summary['total']}%)")
    console.print(f"hourglass Pending:         {summary['pending']:>15} | ({summary['pending']}/{summary['total']}%)")
    console.print(f"warning Overdue:         {summary['overdue']:>15} | ({summary['overdue']}/{summary['pending']}% of pending)" if summary['pending'] > 0 else f"warning Overdue:         {summary['overdue']:>15}")
    console.print()

    # Priority breakdown
    if tasks:
        console.print("Priority Breakdown:")
        high_count = sum(1 for t in tasks if t.priority == Priority.HIGH)
        medium_count = sum(1 for t in tasks if t.priority == Priority.MEDIUM)
        low_count = sum(1 for t in tasks if t.priority == Priority.LOW)
        total = len(tasks)

        console.print(f"red circle High:            {high_count:>15} | ({high_count}/{total}%)")
        console.print(f"yellow circle Medium:          {medium_count:>15} | ({medium_count}/{total}%)")
        console.print(f"green circle Low:             {low_count:>15} | ({low_count}/{total}%)")
        console.print()

    console.print("=" * 60)

    # All completed celebration
    if summary['completed'] > 0 and summary['pending'] == 0:
        console.print()
        console.print("celebration All tasks completed!")


def handle_exit(tasks: List[Task]) -> None:
    """Handle Exit feature (User Story 8)."""
    console.print()
    console.print("[0] Exit")
    console.print("-" * 50)
    console.print()
    console.print("Goodbye!")
    console.print()
    console.print("Task Session Summary:")
    console.print("─────────────────────")
    summary = get_summary(tasks)
    console.print(f"Total Tasks: {summary['total']}")
    console.print(f"Completed: {summary['completed']}")
    console.print(f"Pending: {summary['pending']}")
    console.print()
    console.print("floppy Note: Tasks are saved in-memory and will be lost when app exits.")
    console.print("   Enable persistence in Phase 2 for permanent storage.")
    console.print()
    console.print("=" * 60)


def main() -> None:
    """Main application loop."""
    tasks: List[Task] = []

    while True:
        display_menu(tasks)
        choice = get_menu_choice()

        if choice is None:
            print_error("Invalid choice. Please enter a number between 0 and 7.")
            wait_for_enter()
            continue

        if choice == 0:
            handle_exit(tasks)
            break
        elif choice == 1:
            handle_add_task(tasks)
            wait_for_enter()
        elif choice == 2:
            handle_delete_task(tasks)
            wait_for_enter()
        elif choice == 3:
            handle_update_task(tasks)
            wait_for_enter()
        elif choice == 4:
            handle_view_tasks(tasks)
            wait_for_enter()
        elif choice == 5:
            handle_mark_complete(tasks)
            wait_for_enter()
        elif choice == 6:
            handle_search_tasks(tasks)
            wait_for_enter()
        elif choice == 7:
            handle_task_summary(tasks)
            wait_for_enter()
        else:
            print_error("Invalid choice. Please enter a number between 0 and 7.")
            wait_for_enter()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print()
        console.print()
        console.print("Goodbye!")
