from fastapi import APIRouter, Depends
from app.authors.crud import AuthorDAO
from app.books.crud import BookDAO
from app.books.schemas import Book, BookCreate, BookUpdate
from typing import Annotated
from  app.users.models import User
from app.users.dependencies import get_current_user
from app.books.exceptions import (
    BookByIdNotFound,
    BookNotCreated,
    BookNotUpdate,
    NotDeletedById,
    AuthorByIdNotFound,
)

router = APIRouter(
    prefix="/books",
    tags=["Книги 📚"],
)


@router.get("/", response_model=list[Book])
async def get_books(skip: int = 0, limit: int = 100):
    books = await BookDAO.find_all()
    for book in books:
        author = await AuthorDAO.find_id(book.author_id)
        book.author = author

    return books[skip : skip + limit]


@router.get("/{book_id}/", response_model=Book)
async def get_book(book_id: int):
    book = await BookDAO.find_id(id=book_id)
    if book is None:
        raise BookByIdNotFound
    author = await AuthorDAO.find_id(book.author_id)
    book.author = author
    return book


@router.post("/", response_model=Book)
async def create_book(user: Annotated[User,Depends(get_current_user)], book: Annotated[BookCreate, Depends()]):
    author = await AuthorDAO.find_id(book.author_id)
    if author is None:
        raise AuthorByIdNotFound
    created = await BookDAO.add(**book.model_dump())
    if created is None:
        raise BookNotCreated

    created.author = author
    return created



@router.put("/{book_id}/")
async def update_book(book_id: int, book_update: Annotated[BookUpdate, Depends()]):
    author = await AuthorDAO.find_id(book_update.author_id)
    if author is None:
        raise AuthorByIdNotFound

    updated = await BookDAO.update(
        book_id, **book_update.model_dump(exclude_unset=True)
    )

    if updated is None:
        raise BookNotUpdate

    updated.author = author
    return {"detail": "Книга успешно обновлена."}


@router.delete("/{book_id}/")
async def delete_book(book_id: int):
    deleted = await BookDAO.delete(id=book_id)
    if deleted is None:
        raise NotDeletedById
    return {"detail": "Книга успешно удалена."}
