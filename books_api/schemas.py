from typing import Optional
from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str
    genre: str
    author: str
    description: str
    year: int
    rating: int = Field(ge=1, le=10, description="Rating from 1 to 10")


class BookResponse(BaseModel):
    id: int
    title: str
    genre: str
    author: str
    description: str
    year: int


class AuthorCreate(BaseModel):
    name: str
    age: int
    bio: str


class AuthorResponse(BaseModel):
    id: int
    name: str
    age: int
    bio: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None


class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    bio: Optional[str] = None
