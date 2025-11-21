# Books and Authors API 📚

A RESTful API built with FastAPI for managing books and authors. This project demonstrates modern Python web development with proper validation, documentation, and REST principles.

## 🚀 Features

- **CRUD Operations**: Create, read, update, and delete books and authors
- **Search Functionality**: Search books by title with case-insensitive matching
- **Data Validation**: Strict input validation using Pydantic schemas
- **Auto-generated Documentation**: Interactive Swagger UI and ReDoc
- **RESTful Design**: Clean API endpoints following REST principles
- **Error Handling**: Proper HTTP status codes and error messages

## 📋 API Endpoints

### Books Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/books` | Get all books | |
| `GET` | `/books/search` | Search books by title | `title` (query parameter) |
| `POST` | `/books/` | Create new book entry | JSON body |
| `PATCH` | `/books/{book_id}` | Update book information | `book_id` (path parameter), JSON body |
| `DELETE` | `/books/{book_id}` | Delete book | `book_id` (path parameter) |

### Authors Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/authors` | Get all authors | |
| `POST` | `/authors/` | Create new author entry | JSON body |
| `PATCH` | `/authors/{author_id}` | Update author information | `author_id` (path parameter), JSON body |
| `DELETE` | `/authors/{author_id}` | Delete author | `author_id` (path parameter) |

## 🛠️ Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping
- **Pydantic** - Data validation and settings management
- **Python** - Programming language
- **Type Hints** - Enhanced code clarity and IDE support

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd books-authors-api

2. Install dependencies
   ```
   pip install fastapi uvicorn
4. Run the application
   ```
   uvicorn main:app 
6. Access the API
API: http://localhost:8000
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc



