import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.models.task import Task, SubTask 
from datetime import datetime

# Create a test task 
task = Task(
    title = "Go to groceries store",
    description = "Go to the store at 44 avn",
    priority = "High"
)

print(f"ID: {task.id}")
print(f"Title: {task.title}")
print(f"Created: {task.created_at}")
