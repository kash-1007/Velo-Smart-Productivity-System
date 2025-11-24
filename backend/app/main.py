from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Velo backend is running smoothly."}
