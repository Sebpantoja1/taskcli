from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID

class SubTask(BaseModel):
    title: str
    is_done: bool = False

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str]
    state: str = "Todo" # Todo, In Progress, Done
    priority: str = "Medium" #Low, Medium, High
    subtasks: List[SubTask] = []
    createdAt: datetime = Field(default_factory= datetime.now) 
    updatedAt: datetime = Field(default_factory= datetime.now)

    @property
    def progress(self) -> float:
        if not self.subtasks:
            return 1.0 if self.state == "Done" else 0.0
        done = sum(1 for st in self.subtasks if st.is_done)
        return done/len(self.subtasks)
    