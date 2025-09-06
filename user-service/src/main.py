import asyncio
from faststream import FastStream
from faststream.kafka import KafkaBroker

from src.config import settings
from src.handlers import router

broker = KafkaBroker(f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}')
broker.include_router(router)

app = FastStream(broker)

if __name__ == "__main__":
    asyncio.run(app.run())
