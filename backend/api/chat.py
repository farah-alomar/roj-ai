from fastapi import APIRouter
from pydantic import BaseModel

from database.memory import create_session, save, load_last
from services.intent_service import detect_intent
from services.language_service import detect_language
from services.prompt_service import build_prompt
from services.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


@router.post("/chat")
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        return {
            "answer": "Please enter a message.",
            "session_id": request.session_id
        }

    session_id = request.session_id

    if session_id is None:
        session_id = create_session()

    context = load_last(session_id, 10)

    history = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in context
    )

    language = detect_language(message)
    intent = detect_intent(message)

    prompt = build_prompt(
        history=history,
        message=message,
        intent=intent,
        language=language
    )

    save(session_id, "user", message)

    answer = ask_gemini(prompt)

    save(session_id, "assistant", answer)

    return {
        "answer": answer,
        "session_id": session_id
    }