from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.feedback import router as feedback_router

app = FastAPI(
    title="RojAI",
    version="0.1"
)

# السماح للواجهة الأمامية بالاتصال مع الـ Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تسجيل الـ Routers
app.include_router(chat_router)
app.include_router(feedback_router)


@app.get("/")
def home():
    return {
        "project": "RojAI",
        "status": "Running"
    }

