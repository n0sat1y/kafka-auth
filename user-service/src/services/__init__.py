import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.repositories import UserRepository
from src.schemas import (
    GenericCreateResponseSchema, GenericGetResponseSchema,
    GenericUpdateResponseSchema,
    CreateUserRequestSchema, UpdateUserRequestSchema
)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository):
        self.repo = repository

    async def get(self, user_id: int) -> dict:
        try:
            user = await self.repo.get(user_id)
            if not user:
                logger.warning('Пользователь не найден: %s', user_id)
                return GenericGetResponseSchema(
                    status='error', code=404, error_message='User not found'
                )
            return GenericGetResponseSchema(
                status='success', code=200, data=user.__dict__
            )
        except Exception as e:
            logger.error('Ошибка при получении пользователя', e)
            return GenericGetResponseSchema(
                status='error', code=500, error_message='An error occurred during getting user'
            )

    async def get_by_username(self, username: str) -> dict:
        try:
            user = await self.repo.get_by_username(username)
            if not user:
                logger.warning('Пользователь не найден: %s', username)
                return GenericGetResponseSchema(
                    status='error', code=404, error_message='User not found'
                )
            return GenericGetResponseSchema(
                status='success', code=200, data=user.__dict__
            )
        except Exception as e:
            logger.error('Ошибка при получении пользователя', e)
            return GenericGetResponseSchema(
                status='error', code=500, error_message='An error occurred during getting user'
            )

    async def create(self, user_schema: CreateUserRequestSchema) -> dict:
        try:
            user_data = user_schema.model_dump()
            user = await self.repo.create(user_data)
            return GenericCreateResponseSchema(
                status='success',
                code=201,
                data=user.__dict__
            )
        except IntegrityError as e:
            logger.warning('Попытка повторного создания пользователя: %s', user_schema.username)
            return GenericCreateResponseSchema(
                status='error', code=400, error_message='This user has already been created'
            )
        except Exception as e:
            logger.error('Ошибка при создании пользователя', e)
            return GenericCreateResponseSchema(
                status='error', code=500, error_message='An error occurred during creating user'
            )
        
    async def update(self, user_id: int, user_data: UpdateUserRequestSchema) -> dict:
        try:
            user_dict = user_data.model_dump()
            if not user_dict:
                logger.warning('Были переданы пустые данные: %s', user_id)
                return GenericUpdateResponseSchema(
                    status='error', code=400, error_message='Set some data'
                )
        
            user = await self.repo.get(user_id)
            if not user:
                logger.warning('Пользователь не найден: %s', user_id)
                return GenericUpdateResponseSchema(
                    status='error', code=400, error_message='User not found'
                )
            
            new_user = self.repo.update(user, user_dict)
            return GenericUpdateResponseSchema(
                status='success', code=200, data=new_user.__dict__
            )
        except Exception as e:
            logger.error('Ошибка при обновлении пользователя', e)
            return GenericUpdateResponseSchema(
                status='error', code=500, error_message='An error occurred during updating user'
            )
