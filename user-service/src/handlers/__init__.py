from typing import Annotated
from faststream import Depends
from faststream.kafka import KafkaRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.services import UserService
from src.repositories import UserRepository
from src.core.db import get_session
from src.core.config import settings
from src.schemas import CreateUserSchema, CreateUserResponseSchema


async def user_repository(session: Annotated[AsyncSession, Depends(get_session)]):
    return UserRepository(session)

async def user_service(repo = Depends(user_repository)):
    return UserService(repo)

router = KafkaRouter(prefix=settings.ROUTER_PREFIX)

@router.subscriber('create')
async def create(user_data: CreateUserSchema, _service = Depends(user_service)) -> CreateUserResponseSchema | str:
    response = await _service.create(user_data)
    print(response)
    return response

