from typing import Annotated
from faststream import Depends
from faststream.kafka import KafkaRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.services import UserService
from src.repositories import UserRepository
from src.core.db import get_session
from src.core.config import settings
from src.schemas import (
    GenericCreateResponseSchema, GenericGetResponseSchema,
    GenericUpdateResponseSchema,
    CreateUserRequestSchema, UpdateUserRequestSchema
)

async def user_repository(session: Annotated[AsyncSession, Depends(get_session)]):
    return UserRepository(session)

async def user_service(repo = Depends(user_repository)):
    return UserService(repo)

router = KafkaRouter(prefix=settings.ROUTER_PREFIX)

@router.subscriber('get')
async def get(id: int, _service = Depends(user_service)) -> GenericGetResponseSchema:
    response = await _service.get(id)
    return response

@router.subscriber('get_by_username')
async def get_by_username(username: str, _service = Depends(user_service)) -> GenericGetResponseSchema:
    response = await _service.get_by_username(username)
    return response

@router.subscriber('create')
async def create(user_data: CreateUserRequestSchema, _service = Depends(user_service)) -> GenericCreateResponseSchema:
    response = await _service.create(user_data)
    return response

@router.subscriber('update')
async def update(id: int, user_data: UpdateUserRequestSchema, _service = Depends(user_service)) -> GenericUpdateResponseSchema:
    response = await _service.update(id, user_data)
    return response

