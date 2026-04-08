import json
from pathlib import Path
from typing import List, Optional
from ..models.task import Task 

class DatabaseManager: 
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = Path(file_path)
    
    def save(self, tasks: List[Task]) ->None:
        # Save list of tasks to JSON file
        data = [task.model_dump(mode='json') for task in tasks]
        self.file_path.write_text(json.dumps(data, indent=2, default=str))
    
    def load(self) -> List[Task]:
        # Load tasks from JSON file
        if not self.file_path.exists():
            return []
        
        content = self.file_path.read_text()
        if not content.strip():
            return []
        
        data = json.loads(self.file_path.read_text())
        return [Task(**item) for item in data]
    
    def add(self, task: Task) -> List[Task]:
        #Add a task and save
        tasks = self.load()
        tasks.append(task)
        self.save(tasks)
        return tasks 
    
    def update(self, task: Task) -> List[Task]:
        # Update an existing task
        tasks = self.load()
        for i, t in enumerate(tasks):
            if t.id == task.id:
                tasks[i] = task
                break 
        self.save(tasks)
        return tasks
    
    def delete(self, task_id: str) -> List[Task]:
        # Delete a task by ID
        tasks = self.load()
        tasks = [t for t in tasks if str(t.id) != task_id]
        self.save(tasks)
        return tasks