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
