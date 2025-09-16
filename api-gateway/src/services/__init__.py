import json
from fastapi import HTTPException

from src.core.rpc import RPCWorker
from src.schemas import (
    CreateUserSchema, GenericTokenResponseSchema, GenericGetResponseSchema
)

class APIService:
    def __init__(self, worker: RPCWorker):
        self.worker = worker

    async def create_user(self, user_data: CreateUserSchema):
        response = await self.worker.request(user_data.model_dump(), 'auth_create_user')
        response = GenericGetResponseSchema.model_validate_json(response)
        if response.status == 'success':
            return response.data
        raise HTTPException(status_code=response.code, detail=response.error_message)
    
    async def authenticate(self, user_data: CreateUserSchema):
        response = await self.worker.request(user_data.model_dump(), 'auth_user')
        response = GenericTokenResponseSchema.model_validate_json(response)
        if response.status == 'success':
            return response.data
        raise HTTPException(status_code=response.code, detail=response.error_message)
