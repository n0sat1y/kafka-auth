import json
from faststream.kafka import KafkaRouter

from src.schemas import (
    GenericTokenResponseSchema, CreateUserSchema,
    GenericGetResponseSchema
)
from src.utils import hash_password, validate_password, encode_access_jwt, encode_refresh_jwt
from src.core.rpc import rpc_worker
from src.core.config import settings

router = KafkaRouter(prefix=settings.ROUTER_PREFIX)

@router.subscriber('create_user')
async def create_user(user_data: CreateUserSchema):
    user_data.password = hash_password(user_data.password)
    data = json.loads(await rpc_worker.request(user_data.model_dump(), 'user_create'))
    return data

@router.subscriber('user')
async def auth_user(user_data: CreateUserSchema) -> GenericTokenResponseSchema:
    data = await rpc_worker.request(user_data.username, 'user_get_by_username')
    data = GenericGetResponseSchema.model_validate_json(data)
    if data.status == 'success':
        user_id = data.data.id
        password = data.data.password
        if validate_password(user_data.password, password):
            return GenericTokenResponseSchema(
                status=data.status,
                code=data.code,
                data={
                    'access': encode_access_jwt({'sub': user_id}),
                    'refresh': encode_refresh_jwt({'sub': user_id})
                }
            )
        else:
            return GenericTokenResponseSchema(
                status='error', code=400, error_message='Wrong password'
            )
    return data
