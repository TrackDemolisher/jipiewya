from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.database import init_db
from app.routes.auth import router as auth_router
from app.routes.events import router as events_router
from app.routes.documents import student_router, teacher_router

app = FastAPI(title="СтудПортфолио")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

app.include_router(auth_router)
app.include_router(events_router)
app.include_router(student_router)
app.include_router(teacher_router)

DATA_DIR = os.environ.get("DATA_DIR", ".")
UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

FRONTEND_FILE = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def serve_frontend():
    if os.path.exists(FRONTEND_FILE):
        return FileResponse(FRONTEND_FILE, media_type="text/html")
    return {"status": "ok", "message": "СтудПортфолио API"}
