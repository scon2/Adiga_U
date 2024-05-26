from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Spot(BaseModel):
    id: int
    name: str = None
    location: str = None
    time: str = None
    tags: str = None
    description: str = None
    good: int = None


db = []

@app.get("/")
async def message():
    return '어디가유 데이터 서버입니당 spots'

@app.post("/spots/")
async def create_spot(spot: Spot):
    db.append(spot)
    return spot

@app.get("/spots")
async def read_spot():
    return db

@app.get("/spots/{spot_id}")
async def read_splot(spot_id: int):
    for spot in db:
        if spot.id == spot_id:
            return spot
