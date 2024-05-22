from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Location(BaseModel):
    id: int
    name: str
    tag: str
    good: int
    

db = []

@app.get("/")
async def m():
    return '안녕하세요'

@app.post("/locations/", response_model=Location)
async def create_location(location: Location):
    db.append(location)
    return location

@app.get("/locations/", response_model=List[Location])
async def read_location():
    return db

@app.get("/locations/{location_id}",response_model=Location)
async def read_location(location_id: int):
    for location in db:
        if location.id == location_id:
            return location

