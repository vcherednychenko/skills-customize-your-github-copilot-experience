# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to build a simple REST API using FastAPI, including route creation, request validation, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Build Core API Endpoints

#### Description
Create a FastAPI app that manages a small in-memory list of books. Implement endpoints to list all books and fetch a single book by ID.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book or a 404 error if not found


### 🛠️ Add Create and Update Operations

#### Description
Extend the API with data validation and write operations. Add endpoints to create a new book and update an existing one.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data
- Implement `POST /books` to add a new book with an auto-incremented ID
- Implement `PUT /books/{book_id}` to update an existing book or return 404 if missing
