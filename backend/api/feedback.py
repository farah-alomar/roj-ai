from fastapi import APIRouter
from pydantic import BaseModel

from database.feedback import save_feedback

router = APIRouter()


class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int
    comment: str = ""


@router.post("/feedback")
def feedback(data: FeedbackRequest):

    save_feedback(
        data.question,
        data.answer,
        data.rating,
        data.comment
    )

    return {
        "success": True
    }