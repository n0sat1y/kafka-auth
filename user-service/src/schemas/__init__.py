from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    username: str
    password: bytes

class CreateUserResponseSchema(BaseModel):
    id: int
    
