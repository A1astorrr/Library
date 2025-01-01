from fastapi import UploadFile, APIRouter
import shutil


router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"],
)

@router.post("/books")
async  def add_book_image(name: int, file:UploadFile):
    with open(f"app/static/images/{name}.webp", "+wb") as file_object:
        shutil.copyfileobj(file.file, file_object)