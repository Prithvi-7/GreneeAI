from fastapi import APIRouter
from app.schemas.ai_chatbot import ChatRequest, ChatResponse
from app.services.ai_chatbot_service import get_ai_response

router = APIRouter(
    prefix="/ai-chatbot",
    tags=["AI Chatbot"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = get_ai_response(request.question)

    return ChatResponse(
        answer=answer
    )