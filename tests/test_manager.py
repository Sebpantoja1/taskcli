import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.models.task import Task 
from src.database.manager import DatabaseManager

project_root = Path(__file__).parent.parent
db = DatabaseManager(str(project_root / "data" / "test_tasks.json" ))

# add task
task = Task(
    title = "Managed Task 3",
    description = "Testing the json"
)
tasks = db.add(task)
print(f"Added {len(tasks)} tasks")
print(f"Title: {task.title}")

