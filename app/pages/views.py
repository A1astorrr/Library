from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.books.views import get_books

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
)


templates = Jinja2Templates(directory="app/templates")


@router.get("/books")
async def get_books_page(request: Request, books=Depends(get_books)):
    return templates.TemplateResponse(name="books.html", context={"request": request, "books": books})
