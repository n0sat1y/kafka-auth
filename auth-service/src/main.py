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
    print('Отправляем данные')
    data = await rpc_worker.request({'username': 'eblan-kavach', 'password': 'some-pass'}, 'auth_create_user')
    print(f"{data=}")

if __name__ == "__main__":
    run(app.run())
