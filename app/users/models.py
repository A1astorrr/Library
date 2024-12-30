from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.users.schemas import UserRole

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, info={"description": "Уникальный идентификатор пользователя"})
    email: Mapped[str] = mapped_column(nullable=False, info={"description": "Email пользователя"})
    hashed_password: Mapped[str] = mapped_column(nullable=False, info={"description": "Хэшированный пароль пользователя"})
    role: Mapped[UserRole] = mapped_column(nullable=False, info={"description": "Роль пользователя (admin, user, editor)"})
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"
