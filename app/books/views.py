from fastapi import APIRouter, Depends
from app.books.crud import BookDAO
from app.books.schemas import Book, BookCreate, BookUpdate
from typing import Annotated
from app.books.exceptions import (
    BookByIdNotFound,
    BookNotCreated,
    BookNotUpdate,
    NotDeletedById,
)

router = APIRouter(
    prefix="/books",
    tags=["Книги 📚"],
)


@router.get("/", response_model=list[Book])
async def get_books(skip: int = 0, limit: int = 100):
    books = await BookDAO.get_all()
    return books[skip : skip + limit]


@router.get("/{book_id}/", response_model=Book)
async def get_book(book_id: int):
    book = await BookDAO.get_id(book_id)
    if book is None:
        raise BookByIdNotFound
    return book

@router.post("/", response_model=Book)
async def create_book(book: Annotated[BookCreate, Depends()]):
    created = await BookDAO.add(**book.model_dump())
    if created is None:
        raise BookNotCreated
    return created

@router.put("/{book_id}/")
async def update_book(book_id: int, todo_update: Annotated[BookUpdate, Depends()]):
    updated = await BookDAO.update(book_id, **todo_update.model_dump(exclude_unset=True))
    if updated is None:
        raise BookNotUpdate
    return {"detail": "Книга успешно обновлена."}

@router.delete("/{book_id}/")
async def delete_book(book_id: int):
    deleted = await BookDAO.delete(id=book_id)
    if deleted is None:
        raise NotDeletedById
    return {"detail":"Книга успешно обновлнеа"}
