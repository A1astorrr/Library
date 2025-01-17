import pytest
from app.users.crud import UsersDAO



@pytest.mark.parametrize(
    "email, exists",
    [("oleg@mail.ru", True), ("maks@mail.ru", True), ("...", False)],
)
@pytest.mark.asyncio(loop_scope="session")
async def test_find_user_by_id(email, exists):
    user = await UsersDAO.find_one_or_none(email=email)

    if exists:
        assert user
        assert user.email == email
    else:
        assert not user



