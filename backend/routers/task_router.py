from fastapi import APIRouter
from models.task_model import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# temporary in-memory list (database will come later)
fake_tasks_db = [
    Task(id=1, title="Learn FastAPI", completed=False),
    Task(id=2, title="Plan project architecture", completed=True),
]

@router.get("/")
def get_tasks():
    return fake_tasks_db
