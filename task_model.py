from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    due_date: Optional[str] = None
    priority: int = 3
    cost: float = 0.0
    metadata: dict = field(default_factory=dict)

def create_task(next_id, title, **kwargs):
    return Task(id=next_id, title=title, **kwargs)
