import datetime
from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from typing import Annotated

created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True, nullable=True)
    annotation: Mapped[str] = mapped_column(nullable=True)
    date_publishing: Mapped[created_at]
    genre: Mapped[str]= mapped_column(nullable=True)
    publisher: Mapped[str]= mapped_column(nullable=True)
    image_id: Mapped[int] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE")) 
    author = relationship("Author", back_populates="books")
    
    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title='{self.title}', annotation='{self.annotation}', date_publishing='{self.date_publishing}')>"
    
    def __str__(self) -> str:
        return f"Книга: {self.title}"