from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import datetime
import uvicorn

app = FastAPI()



class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int  = Field(..., gt=1800)
    rating: float = Field(..., ge=0.0, le=10.0)

    @field_validator('release_year')
    @classmethod
    def check_year_not_in_future(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError("Рік випуску не може бути в майбутньому")
        return v

movies_db: List[Movie] = []

@app.get("/movies", response_model=List[Movie])
def get_movies():
    return movies_db

@app.post("/movies", response_model=Movie, status_code=201)
def add_movie(movie: Movie):
    if any(existing.id == movie.id for existing in movies_db):
        raise HTTPException(status_code=400, detail="Фільм з таким ID вже існує")
    movies_db.append(movie)
    return movie

@app.get("/movies/{id}", response_model=Movie)
def get_movie(id: int):
    for movie in movies_db:
        if movie.id == id:
            return movie
    raise HTTPException(status_code=404, detail="Фільм не знайдено")

@app.delete("/movies/{id}", status_code=204)
def delete_movie(id: int):
    for i, movie in enumerate(movies_db):
        if movie.id == id:
            del movies_db[i]
            return
    raise HTTPException(status_code=404, detail="Фільм не знайдено")
