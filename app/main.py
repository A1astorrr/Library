from fastapi import FastAPI
import uvicorn
from app.books.views import router as books_router
from app.authors.views import router as authors_router
from app.users.views import router as auth_router
from app.pages.views import router as router_pages
from  app.images.views import router as router_images
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(books_router)
app.include_router(authors_router)
app.include_router(auth_router)


app.include_router(router_pages)
app.include_router(router_images)

@app.get("/")
def welcome():
    return {"message": "Welcome to Library"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)