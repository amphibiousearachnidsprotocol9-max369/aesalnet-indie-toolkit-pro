from fastapi import FastAPI
from src.status import get_status

app = FastAPI()

@app.get("/status")
def status():
    return get_status()
