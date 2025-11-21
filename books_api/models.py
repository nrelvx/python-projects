from sqlalchemy import Column, ForeignKey, Integer, String, Text
from db import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    genre = Column(String(15))
    author = Column(String)
    description = Column(Text)
    year = Column(Integer)


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    bio = Column(Text)
