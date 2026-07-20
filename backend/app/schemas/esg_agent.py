from pydantic import BaseModel


class ESGAgentRequest(BaseModel):
    query: str


class ESGAgentResponse(BaseModel):
    response: str
    action: str