from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# class Location(BaseModel):
#     id: int
#     name: str
#     tag: str
#     good: int


db = []

@app.get("/")
async def message():
    return '어디가유 데이터 서버입니당'

@app.post("/locations/")
async def create_location(location: list):
    db.extend(location)
    return location

@app.get("/locations/")
async def read_location():
    return db

@app.get("/locations/{location_id}")
async def read_location(location_name: str):
    for location in db:
        if location['name'] == location_name:
            return location

