from fastapi import APIRouter
from app.schemas.esg_agent import (
    ESGAgentRequest,
    ESGAgentResponse
)
from app.services.esg_agent_service import (
    process_esg_query
)

router = APIRouter(
    prefix="/esg-agent",
    tags=["Autonomous ESG Agent"]
)


@router.post("/", response_model=ESGAgentResponse)
def esg_agent(request: ESGAgentRequest):

    result = process_esg_query(
        request.query
    )

    return ESGAgentResponse(
        response=result["response"],
        action=result["action"]
    )