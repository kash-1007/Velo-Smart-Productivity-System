from fastapi import FastAPI
from routers.task_router import router as task_router
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Kashish, your backend is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Velo Backend"}

# include the router
app.include_router(task_router)