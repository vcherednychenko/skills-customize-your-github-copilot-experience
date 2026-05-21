# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


# In-memory data store
books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
]


@app.get("/books")
def get_books():
    # TODO: Return all books
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return a single book by ID or raise HTTPException(status_code=404)
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookInput):
    # TODO: Add a new book with an auto-incremented ID and return it
    next_id = max((item["id"] for item in books), default=0) + 1
    new_book = {"id": next_id, "title": book.title, "author": book.author}
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update an existing book or raise HTTPException(status_code=404)
    for item in books:
        if item["id"] == book_id:
            item["title"] = book.title
            item["author"] = book.author
            return item
    raise HTTPException(status_code=404, detail="Book not found")


# Run locally:
# uvicorn starter-code:app --reload
