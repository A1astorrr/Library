from fastapi import APIRouter, HTTPException, Response, status, Depends
from app.users.models import User
from app.users.schemas import SUserAuth, SUserAuthAdmin
from app.users.crud import UsersDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from typing import Annotated
from app.users.dependencies import get_current_admin_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

# регистрация пользователя
@router.post("/register")
async def register_user(user_data: Annotated[SUserAuthAdmin, Depends()]):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password, role=user_data.role)
    return {"detail": "Пользователь успешно зарегестрирован"}

# авторизация пользователя
@router.post("/login")
async def login_user(response: Response, user_data: Annotated[SUserAuth, Depends()]):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("books_access_token", access_token, httponly=True)
    return {"access_token": access_token}

# удаление  пользователя из системы(выход)
@router.post("logout")
async def logout_user(response: Response):
    response.delete_cookie("books_access_token")
    return {"detail": "Пользователь вышел из системы"}

# данные о текущем пользователе
@router.get("/all")
async def read_users_all(current_user: User = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()