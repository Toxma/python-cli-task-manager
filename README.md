# Task Manager CLI

A simple CLI-based task manager application built using Python. It allows users to add, list, and delete tasks. Tasks are stored in a `tasks.json` file, and the application provides logging for each action.

## Project Structure

```plaintext
├── README.md
├── requirements.txt
├── task_manager
│   ├── cli.py          # CLI entry point
│   ├── config.py       # Configuration settings (e.g., tasks file path)
│   ├── core.py         # Core business logic (add, list, delete tasks)
│   ├── __init__.py     # Task manager package initializer
│   ├── logger.py       # Logger setup for task manager actions
│   └── test_core.py    # Unit tests for task manager core functionality
├── tests               # Test directory
│   └── test_core.py    # Unit tests for task manager CLI functionality
```

## Installation

To install the dependencies, use pip:

```bash
pip install -r requirements.txt
```

To discover and run all the tests in the `tests` directory, use the following command:

```bash
python -m unittest discover tests
```


### CLI Commands

The task manager provides a few commands to interact with the task list:

1. **List Tasks**

   To list all tasks:

```bash
python -m task_manager.cli list
```


2. **Add Task**

To add a task with a description and priority:

```bash
python -m task_manager.cli add "Task Description" --priority <priority>
```

Example:

```bash
python -m task_manager.cli add "New task" --priority 4
```


3. **Delete Task**

To delete a task by its ID:

```bash
python -m task_manager.cli delete <task_id>
```

Example:

```bash
python -m task_manager.cli delete 1
```