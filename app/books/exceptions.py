from fastapi import HTTPException, status

BookByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Book not found."
)

AuthorByIdNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Author not found."
)

BookNotCreated = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Error in creating the book.",
)

BookNotUpdate = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="The book is not updated.",
)

NotDeletedById = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Book not found."
)

