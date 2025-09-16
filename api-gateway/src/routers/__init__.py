from typing import Annotated
from faststream import Depends
from faststream.kafka.fastapi import KafkaRouter, KafkaBroker

from src.services import APIService
from src.core.config import settings
from src.core.rpc import RPCWorker

router = KafkaRouter(f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}')
broker = router.broker
rpc_worker = RPCWorker(broker, settings.ROUTER_RESPONSE)

def get_service():
    return APIService(rpc_worker)

@router.get('/health_check')
async def health_check():
    return 'Hello'

@router.post('/authenticate')
async def authenticate(
    _service:  Annotated[APIService, Depends(get_service)]
):
    return {'success': True}
    


