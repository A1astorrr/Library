from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.users.schemas import UserRole

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(nullable=False)
    
    def __repr__(self) -> str:
        return f"<Author(id={self.id}, email='{self.email}', role='{self.role}')>"