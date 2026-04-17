from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from backend.database import engine, Base
from backend.routers import users, tasks
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def serve_frontend():
    # Serve the frontend/index.html right at the URL root so it's a single server experience
    return FileResponse(os.path.join("frontend", "index.html"))
