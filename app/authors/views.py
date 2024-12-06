from fastapi import APIRouter, Depends
from app.authors.crud import AuthorDAO
from app.authors.schemas import Author, AuthorCreate, AuthorUpdate
from typing import Annotated
from app.authors.exceptions import (
    AuthorByIdNotFound,
    AuthorNotCreated,
    AuthorNotUpdate,
    NotDeletedById,
)


router = APIRouter(
    prefix="/authors",
    tags=["Авторы 📝"],
)


@router.get("/", response_model=list[Author])
async def get_authors(skip: int = 0, limit: int = 100):
    books = await AuthorDAO.get_all()
    return books[skip : skip + limit]


@router.get("/{author_id}/", response_model=Author)
async def get_author(author_id: int):
    book = await AuthorDAO.get_id(author_id)
    if book is None:
        raise AuthorByIdNotFound
    return book


@router.post("/", response_model=Author)
async def create_author(author: Annotated[AuthorCreate, Depends()]):
    created = await AuthorDAO.add(**author.model_dump())
    if created is None:
        raise AuthorNotCreated
    return created


@router.put("/{author_id}/")
async def update_author(
    author_id: int, todo_update: Annotated[AuthorUpdate, Depends()]
):
    updated = await AuthorDAO.update(
        author_id, **todo_update.model_dump(exclude_unset=True)
    )
    if updated is None:
        raise AuthorNotUpdate
    return {"detail": "Автор успешно обновлен."}


@router.delete("/{author_id}/")
async def delete_author(author_id: int):
    deleted = await AuthorDAO.delete(id=author_id)
    if deleted is None:
        raise NotDeletedById
    return {"detail": "Автор успешно удален."}
