from typing import Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import UserModel

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict[str: Any]) -> None:
        try:
            user = UserModel(**data)
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
            return user
        except Exception as err:
            await self.session.rollback()
            raise err
        
    async def get(self, id: int) -> UserModel:
        try:
            res = await self.session.execute(select(UserModel).where(UserModel.id == id))
            return res.scalar_one_or_none()
        except Exception as err:
            await self.session.rollback()
            raise err
        
    async def update(self, user: UserModel, data_to_update: dict) -> UserModel:
        try:
            for key, value in data_to_update.items():
                setattr(user, key, value)
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
            return user
        except Exception as e:
            await self.session.rollback()
            raise e
    
