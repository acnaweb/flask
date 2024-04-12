from flask_openapi3 import APIBlueprint
from flask_openapi3 import Tag
from pydantic import BaseModel, Field
from typing import Optional
from src.config import API_URL_PREFIX, security

tag = Tag(name="Rota1", description="Operações de Rota1")

api = APIBlueprint(
    "rota1",
    __name__,
    abp_tags=[tag],
    abp_security=security,
    url_prefix=API_URL_PREFIX,
    # abp_responses={"401": Unauthorized},
    doc_ui=True,
)


class DataBody(BaseModel):
    param1: Optional[int] = Field(..., ge=2, le=4, description="Param1")
    param2: str = Field(None, min_length=2, max_length=4, description="Param1")


@api.post(
    "/rota1", responses={201: {"content": {"text/csv": {"schema": {"type": "string"}}}}}
)
def create(body: DataBody):
    assert body.param1 == 3
    return {"code": 0, "message": "ok"}
