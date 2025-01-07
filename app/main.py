from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from app.admin.views import UsersAdmin, AuthorsAdmin, BooksAdmin
from app.database import engine
import uvicorn
from app.books.views import router as books_router
from app.authors.views import router as authors_router
from app.users.models import User
from app.users.views import router as auth_router
from app.pages.views import router as router_pages
from  app.images.views import router as router_images
from app.admin.auth import authentication_backend

app = FastAPI()
admin = Admin(app, engine, authentication_backend=authentication_backend)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(books_router)
app.include_router(authors_router)
app.include_router(auth_router)

app.include_router(router_pages)
app.include_router(router_images)



admin.add_view(UsersAdmin)
admin.add_view(BooksAdmin)
admin.add_view(AuthorsAdmin)

if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)