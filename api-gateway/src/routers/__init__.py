from typing import Annotated
from faststream import Depends
from faststream.kafka.fastapi import KafkaRouter, KafkaBroker

from src.services import APIService
from src.core.config import settings
from src.core.rpc import RPCWorker
from src.schemas import CreateUserSchema

router = KafkaRouter(f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}')
broker = router.broker
rpc_worker = RPCWorker(broker, settings.ROUTER_RESPONSE)

def get_service():
    return APIService(rpc_worker)

@router.get('/health_check')
async def health_check():
    return 'Hello'

@router.post('/create_user', response_model_exclude_none=True)
async def create_user(
    user_data: CreateUserSchema
):
    return await get_service().create_user(user_data)

@router.post('/authenticate', response_model_exclude_none=True)
async def authenticate(
    user_data: CreateUserSchema
):
    return await get_service().authenticate(user_data)
    


