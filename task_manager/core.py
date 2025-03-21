import json
import os
from task_manager.logger import setup_logger
from task_manager.config import TASKS_FILE

logger = setup_logger()

def load_tasks():
    """Load tasks from the JSON file, handling empty or missing files."""
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r") as file:
            data = file.read().strip()  # Remove whitespace
            if not data:  # Handle empty file case
                return []
            return json.loads(data)
    except json.JSONDecodeError:
        print("Error: Corrupt tasks.json file. Resetting to empty list.")
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, priority):
    """Add a task."""
    tasks = load_tasks()
    # Check for task with same description (if needed)
    task = {
        "description": description,
        "priority": priority,
        "id": len(tasks) + 1  # Simple increment for task ID
    }
    tasks.append(task)    
    save_tasks(tasks)
    logger.info(f"Task added: {description} (Priority: {priority})")
    print(f"Task added: {description} (Priority: {priority})")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - Priority: {task['priority']}")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()

    # Ensure task_id is valid
    new_tasks = [task for i, task in enumerate(tasks, start=1) if i != task_id]

    if len(new_tasks) == len(tasks):
        logger.error(f"Error: Task ID {task_id} does not exist.")
        print(f"Error: Task ID {task_id} does not exist.")
        return False

    save_tasks(new_tasks)
    logger.info(f"Task {task_id} deleted.")
    print(f"Task {task_id} deleted.")
    return True