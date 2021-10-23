from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import movie

router = APIRouter(
    prefix = "/movie",
    tags = ["movie"]
)

@router.get('/', response_model = List[schemas.Movie])
def all(db: Session = Depends(database.get_db)):
    return movie.get_all()

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Movie, db: Session = Depends(database.get_db)):
    return movie.create(request, db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return movie.destroy(id, db)

@router.put('/{id}', status_code=  status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Movie, db: Session = Depends(database.get_db)):
    return movie.update(id,request,db)