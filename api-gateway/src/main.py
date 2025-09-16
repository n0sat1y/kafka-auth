import uvicorn
from fastapi import FastAPI

from src.routers import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        reload=True
    )
