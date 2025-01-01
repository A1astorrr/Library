import datetime
from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    surname: Mapped[str] = mapped_column(index=True)
    date_birth: Mapped[datetime.date] = mapped_column(Date, nullable=True)
    biography: Mapped[str] = mapped_column(nullable=True)
    image_id: Mapped[int] = mapped_column(nullable=True)
    books = relationship("Book", back_populates="author")

    def __repr__(self) -> str:
        return f"<Author(id={self.id}, name='{self.name}', surname='{self.surname}', date_birth='{self.date_birth}')>"
