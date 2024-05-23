from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Location(BaseModel):
    name: str
    tag: str
    good: int


db = []

@app.get("/")
async def message():
    return '어디가유 데이터 서버입니당'

@app.post("/locations/")
async def create_location(location: Location):
    db.append(location)
    return location

@app.get("/locations/")
async def read_location():
    return db

@app.get("/locations/{location_name}")
async def read_location(location_name: str):
    for location in db:
        if location.name == location_name:
            return location

