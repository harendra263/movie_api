from pydantic import BaseModel
from typing import List, Optional


class MovieBase(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

class Movie(MovieBase):
    class Config():
        orm_mode = True
        
