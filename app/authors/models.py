import datetime
from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, info={"description": "Уникальный идентификатор автора"})
    name: Mapped[str] = mapped_column(index=True, info={"description": "Имя автора"})
    surname: Mapped[str] = mapped_column(index=True, info={"description": "Фамилия автора"})
    date_birth: Mapped[datetime.date] = mapped_column(Date, nullable=True, info={"description": "Дата рождения автора"})
    biography: Mapped[str] = mapped_column(nullable=True, info={"description": "Биография автора"})

    books = relationship("Book", back_populates="author")

    def __repr__(self) -> str:
        return f"<Author(id={self.id}, name='{self.name}', surname='{self.surname}', date_birth='{self.date_birth}')>"
