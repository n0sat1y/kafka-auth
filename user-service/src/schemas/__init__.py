from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    username: str
    password: bytes

class CreateUserResponseSchema(BaseModel):
    id: int

class UpdateUserSchema(BaseModel):
    username: str | None = None
    full_name: str | None = None
    media_path: str | None = None

class UpdateUserResponseSchema(UpdateUserSchema):
    id: int
