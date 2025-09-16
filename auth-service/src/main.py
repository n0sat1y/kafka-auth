from asyncio import Future, wait_for, run
from typing import Annotated, Any
from uuid import uuid4

from faststream import FastStream, Context
from faststream.kafka import KafkaBroker, KafkaMessage

from src.core.broker import broker
from src.handlers import router
from src.core.rpc import rpc_worker

app = FastStream(broker)
broker.include_router(router)

@app.after_startup
async def startup():
    await rpc_worker.start()

if __name__ == "__main__":
    run(app.run())
