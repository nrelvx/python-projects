from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="List of books and authors")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# all books
@app.get("/books", response_model=list[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books


# all author
@app.get("/authors", response_model=list[schemas.AuthorResponse])
async def get_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return authors


# search title
@app.get("/books/search", response_model=list[schemas.BookResponse])
async def get_title(
    title: str = Query(..., description="Book title"), db: Session = Depends(get_db)
):
    db_title = db.query(models.Book).filter(models.Book.title.ilike(f"%{title}%")).all()
    return db_title


# add book
@app.post("/books/", response_model=schemas.BookResponse)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# add author
@app.post("/authors/", response_model=schemas.AuthorResponse)
async def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


# update book
@app.patch("/books/{book_id}")
async def update_book(
    book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)
):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    for field, value in book_update.model_dump(exclude_unset=True).items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book


# update author
@app.patch("/authors/{author_id}")
async def update_author(
    author_id: int, author_update: schemas.AuthorUpdate, db: Session = Depends(get_db)
):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    for field, value in author_update.model_dump(exclude_unset=True).items():
        setattr(db_author, field, value)

    db.commit()
    db.refresh(db_author)
    return db_author


# delete book
@app.delete("/books/{book_id}")
async def del_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}


# delete author
@app.delete("/authors/{author_id}")
async def del_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return {"message": "Author deleted successfully"}
