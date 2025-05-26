from pydantic import BaseModel

class Book(BaseModel):
    id: int
    year: int
    author: str
    title: str
    