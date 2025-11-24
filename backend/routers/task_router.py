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

@router.post("/")
def create_task(task: Task):
    # Generate fake auto-increment ID
    task.id = len(fake_tasks_db) + 1
    
    # Add to fake DB list
    fake_tasks_db.append(task)
    #to run this, we will go to the server and will add /docs at the end , there we will go to the post request , and will add our demo data in the form of json.
    return {
        "message": "Task created successfully",
        "task": task
    }

