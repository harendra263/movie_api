from fastapi import Depends, HTTPException, status
from .. import schemas, models, database
from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).all()
    return movie


def create(request: schemas.Movie, db: Session = Depends(database.get_db)):
    new_movie = models.Movie(name= request.name, plot= request.plot, genres = request.genres, casts = request.casts)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def destroy(id: int, db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id)
    if not movie.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Movie with {id} not found")
    movie.delete(synchronize_session=False)
    db.commit()
    return f"Movie with {id} deleted"

def update_movie(id: int, request: schemas.Movie, db: Session = Depends(database.get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == id)
    if not movie.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Movie with  {id} not found")
    movie.update({"name":request.name, "plot":request.plot, "casts": request.casts, "genres": request.genres})
    db.commit()
    return "updated Successfully"
