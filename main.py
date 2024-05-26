from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import json

app = FastAPI()

class Spot(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = None
    location: Optional[str] = None
    time: Optional[str] = None
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    # good: Optional[int] = Field(default=None)
    # isVideo: Optional[bool] = None
    # pictureURL: Optional[str] = None



db = []

def load_data_from_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i, item in enumerate(data, start=1):
            default_values = {
                "id": i,
                "name": None,
                "location": None,
                "time": None,
                "tags": None,
                "description": None,
                # "good": None,
                # "isVideo": None
            }
            item = {key: item.get(key, default) for key, default in default_values.items()}
            spot = Spot(**item)
            db.append(spot)

@app.get("/")
async def message():
    return '어디가유 데이터 서버입니당 확인용1'

@app.post("/load-data/")
def load_data(file_path: str):
    try:
        load_data_from_json(file_path)
        return {"message": "Data loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/spots/")
def create_spot(spot: Spot):
    for stored_spot in db:
        if stored_spot.id == spot.id:
            raise HTTPException(status_code=400, detail="Spot ID already exists")

    db.append(spot)
    return spot

@app.get("/spots/")
def read_spots():
    return db

# @app.get("/spots/{spot_id}")
# def read_spot(spot_id: int):
#     for spot in db:
#         if spot.id == spot_id:
#             return spot
#     raise HTTPException(status_code=404, detail="Spot not found")