from faststream.kafka import KafkaRouter

from src.schemas import CreateUserSchema
from src.utils import hash_password
from src.core.rpc import rpc_worker
from src.core.config import settings

router = KafkaRouter(prefix=settings.ROUTER_PREFIX)

@router.subscriber('create_user')
async def create_user(user_data: CreateUserSchema):
    user_data.password = hash_password(user_data.password)
    data = await rpc_worker.request(user_data.model_dump(), 'user_create')
    return data
