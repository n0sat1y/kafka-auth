from typing import Literal, Optional
from pydantic import BaseModel

class GenericResponseSchema(BaseModel):
    status: Literal["success", "error"]
    code: int
    error_message: Optional[str] = None
    data: Optional[dict] = None

class CreateUserRequestSchema(BaseModel):
    username: str
    password: bytes

class UserIdSchema(BaseModel):
    id: int

class UpdateUserRequestSchema(BaseModel):
    username: str | None = None
    full_name: str | None = None
    media_path: str | None = None

class GetUserSchema(UserIdSchema, UpdateUserRequestSchema):
    username: str
    password: bytes

class GenericCreateResponseSchema(GenericResponseSchema):
    data: Optional[GetUserSchema] = None

class GenericGetResponseSchema(GenericResponseSchema):
    data: Optional[GetUserSchema] = None

class GenericUpdateResponseSchema(GenericResponseSchema):
    data: Optional[GetUserSchema] = None
