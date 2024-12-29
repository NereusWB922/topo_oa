import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routers.data_router import router as data_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/_next/static", StaticFiles(directory="out/_next/static"), name="static")

app.include_router(data_router)


@app.get("/frontend")
async def get_frontend_index():
    index_path = os.path.join("out/", "index.html")
    return FileResponse(index_path)


@app.get("/")
def health_check():
    return "Navigate to /docs to see the API documentation."
