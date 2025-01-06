from fastapi import APIRouter, Depends
from app.authors.crud import AuthorDAO
from app.books.crud import BookDAO
from app.books.schemas import Book, BookCreate, BookUpdate
from typing import Annotated
from  app.users.models import User
from app.users.dependencies import get_current_user
from app.books.exceptions import (
    BookByIdNotFoundException,
    BookNotCreatedException,
    BookNotUpdateException,
    NotDeletedByIdException,
    AuthorByIdNotFoundException,
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
        raise BookByIdNotFoundException
    author = await AuthorDAO.find_id(book.author_id)
    book.author = author
    return book


@router.post("/", response_model=Book)
async def create_book(user: Annotated[User,Depends(get_current_user)], book: Annotated[BookCreate, Depends()]):
    author = await AuthorDAO.find_id(book.author_id)
    if author is None:
        raise AuthorByIdNotFoundException
    created = await BookDAO.add(**book.model_dump())
    if created is None:
        raise BookNotCreatedException

    if book.title is not None:
        created.title = book.title
    if book.annotation is not None:
        created.annotation = book.annotation
    if book.genre is not None:
        created.genre = book.genre
    if book.publisher is not None:
        created.publisher = book.publisher
    if book.image_id is not None:
        created.image_id = book.image_id
    created.author = author
    return created



@router.put("/{book_id}/")
async def update_book(book_id: int, book_update: Annotated[BookUpdate, Depends()]):
    author = await AuthorDAO.find_id(book_update.author_id)
    if author is None:
        raise AuthorByIdNotFoundException

    updated = await BookDAO.update(
        book_id, **book_update.model_dump(exclude_unset=True)
    )

    if updated is None:
        raise BookNotUpdateException
    
    if book_update.title is not None:
        updated.title = book_update.title
    if book_update.annotation is not None:
        updated.annotation = book_update.annotation
    if book_update.genre is not None:
        updated.genre = book_update.genre
    if book_update.publisher is not None:
        updated.publisher = book_update.publisher
    if book_update.image_id is not None:
        updated.image_id = book_update.image_id
    
    updated.author = author
    return {"detail": "Книга успешно обновлена"}


@router.delete("/{book_id}/")
async def delete_book(book_id: int):
    deleted = await BookDAO.delete(id=book_id)
    if deleted is None:
        raise NotDeletedByIdException
    return {"detail": "Книга успешно удалена"}
