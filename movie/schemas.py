from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

    class Config():
        orm_mode = True

