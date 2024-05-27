from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn
import json

app = FastAPI()

class Food(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = None
    taste: Optional[list[str]] = None

db = []

def load_data_from_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i, item in enumerate(data, start=1):
            default_values = {
                "id": i,
                "name": None,
                "taste": None
            }
            # Replace null values and add default id
            item = {key: item.get(key, default) if item.get(key) is not None else default for key, default in default_values.items()}
            food = Food(**item)
            db.append(food)

@app.get("/")
async def message():
    return '음식 데이터 넣어보는 테스트 서버입니당'

@app.post("/load-data/")
async def load_data(file_path: str):
    try:
        load_data_from_json(file_path)
        return {"message": "Data loaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/foods/")
async def create_food(food: Food):
    for stored_food in db:
        if stored_food.id == food.id:
            raise HTTPException(status_code=400, detail="Spot ID already exists")

    db.append(food)
    return food

@app.get("/foods/")
async def read_foods():
    return db

@app.get("/foods/{food_id}")
async def read_food(food_id: int):
    for food in db:
        if food_id == food.id:
            result = food
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)