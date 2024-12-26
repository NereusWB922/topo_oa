from fastapi import FastAPI
from app.routers.data import router as data_router

app = FastAPI()

app.include_router(data_router)


@app.get("/")
def health_check():
    return "Navigate to /docs to see the API documentation."
