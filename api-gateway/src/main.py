import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routers import router
from src.core.broker import broker

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        reload=True
    )
