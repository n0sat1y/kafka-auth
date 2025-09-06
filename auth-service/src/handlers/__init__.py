from faststream.kafka import KafkaRouter

from src.handlers.user.handler import user_router

router = KafkaRouter(prefix='user_')

router.include_router(user_router)
