import asyncio
from faststream import FastStream
from faststream.kafka import KafkaBroker

from src.core.config import settings
from src.handlers import router
from src.core.broker import broker

broker.include_router(router)

app = FastStream(broker)

if __name__ == "__main__":
    asyncio.run(app.run())
