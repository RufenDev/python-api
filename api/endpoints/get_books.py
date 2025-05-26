import json
from fastapi import APIRouter, Query
from api.schemas.responses import BasicResponse
from typing import Optional, List
from api.schemas.book import Book

router = APIRouter()

@router.get("/book", response_model=BasicResponse)
def get_books(
    author: Optional[str] = Query(
        default=None, 
        description="Filter by author name"
    ),
    title: Optional[str] = Query(
        default=None,
        description="Filter by title matches"
    ),
    year: Optional[int] = Query(
        default=None,
        description="Filter by publication year",
        ge=0,
        le=2025,
    ),
): 
    books: List[Book] = []
    
    with open('example.json', 'r', encoding='utf-8') as file:
        books = [ 
            Book(id=data['id'], author=data['author'], title=data['title'], year=data['year']) 
            for data 
            in json.load(file) 
        ]
    
    # Filter by author
    books = [ 
        book for book in books 
        if not author or author.upper() in book.author.upper()
    ]
    
    # Filter by title
    books = [
        book for book in books
        if not title or title.upper() in book.title.upper()
    ]
    
    # Filter by year
    books = [ 
        book for book in books 
        if not year or book.year == year 
    ]
     
    return BasicResponse(data=books)
