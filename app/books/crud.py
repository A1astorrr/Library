from app.dao.base import BaseDAO
from app.books.models import Book

class BookDAO(BaseDAO):
    model = Book