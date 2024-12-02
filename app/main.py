from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to BookStore"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)