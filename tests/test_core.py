import unittest
import os
import json
from task_manager.core import add_task, load_tasks, delete_task
from task_manager.config import TASKS_FILE

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Reset tasks.json before each test."""
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

    def test_add_task(self):
        """Test adding a task."""
        add_task("Test Task", 2)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)

    def test_delete_task(self):
        """Test deleting a task."""
        add_task("Task to Delete", 1)
        delete_task(1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0) 

if __name__ == "__main__":
    unittest.main()
