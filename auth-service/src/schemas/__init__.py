from typing import Literal, Optional
from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    username: str
    password: str | bytes

class GenericResponseSchema(BaseModel):
    status: Literal["success", "error"]
    code: int
    error_message: Optional[str] = None
    data: Optional[dict] = None

class TokenSchema(BaseModel):
    access: str
    refresh: str

class GetUserSchema(BaseModel):
    id: int
    username: str
    password: bytes
    full_name: str | None = None
    media_path: str | None = None

class GenericTokenResponseSchema(GenericResponseSchema):
    data: Optional[TokenSchema] = None

class GenericGetResponseSchema(GenericResponseSchema):
    data: Optional[GetUserSchema] = None
