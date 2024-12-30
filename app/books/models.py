import datetime
from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from typing import Annotated

created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(20), index=True, info={"description": "Название книги"})
    annotation: Mapped[str] = mapped_column(info={"description": "Аннотация к книге"})
    date_publishing: Mapped[created_at] = mapped_column(info={"description": "Дата публикации книги"})
    genre: Mapped[str] = mapped_column(info={"description": "Жанр книги"})
    publisher: Mapped[str] = mapped_column(info={"description": "Издатель книги"})
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"), info={"description": "ID автора книги"}) 
    author = relationship("Author", back_populates="books")
    
    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title='{self.title}', annotation='{self.annotation}', date_publishing='{self.date_publishing}')>"