from faststream.kafka import KafkaRouter

from src.schemas import CreateUserSchema
from src.utils import hash_password, validate_password, encode_access_jwt, encode_refresh_jwt
from src.core.rpc import rpc_worker
from src.core.config import settings

router = KafkaRouter(prefix=settings.ROUTER_PREFIX)

@router.subscriber('create_user')
async def create_user(user_data: CreateUserSchema):
    user_data.password = hash_password(user_data.password)
    data = await rpc_worker.request(user_data.model_dump(), 'user_create')
    return data

@router.subscriber('user')
async def auth_user(user_data: CreateUserSchema):
    data = await rpc_worker.request(user_data.username, 'user_get_by_username')
    user_id, user_password = data['id'], data['password']
    if not user_id or not validate_password(user_data.password, user_password):
        return 'Wrong user data'
    jwt = {
        'access': encode_access_jwt({'sub': user_id}),
        'refresh': encode_refresh_jwt({'sub': user_id})
    }
    return jwt
