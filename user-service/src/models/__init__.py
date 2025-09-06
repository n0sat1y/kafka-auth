from sqlalchemy.orm import mapped_column, Mapped

from src.core.db import Base


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(nullable=True)
    media_path: Mapped[str] = mapped_column(nullable=True)

