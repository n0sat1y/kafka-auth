import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.repositories import UserRepository
from src.schemas import CreateUserSchema, CreateUserResponseSchema

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository):
        self.repo = repository

    async def create(self, user_schema: CreateUserSchema):
        try:
            user_data = user_schema.model_dump()
            user = await self.repo.create(user_data)
            return user.__dict__
        except IntegrityError as e:
            logger.warning('Попытка повторного создания пользователя: %s', user_schema.username)
            return 'This user has already been created'
        except Exception as e:
            logger.error('Ошибка при создании пользователя', e)
            return 'An error occurred during creating user'
