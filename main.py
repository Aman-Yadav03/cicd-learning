
from fastapi import FastAPI

app = FastAPI(title="CI/CD Learning API")


@app.get("/")
def home():
    return {
    "message": "Hello from my CI/CD learning project!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }