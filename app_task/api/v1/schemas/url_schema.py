from pydantic import BaseModel, field_validator, ConfigDict, Field
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


class ResponseModel(BaseModel):
    url: str | None = Field(default=None)



def answers(
        code_status: status,
        url_text: str,
):
    return JSONResponse(
        status_code=code_status,
        content=ResponseModel(
            url=url_text
        ).__dict__
    )