from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Пользователь уже существует",
)

IncorrectEmailorPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Неверная  почта или пароль",
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Токен  истек",
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Токен отсутствует",
)

IncorrectTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    detail="Неверный токен",
)

UserNotFoundException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, 
)

UserNoRightsException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Нет прав" 
)

CannotAddDataToDatabase = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Не удалось добавить запись"
)