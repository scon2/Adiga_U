from pydantic import BaseModel

# Spot 클래스 정의
class Spot(BaseModel):
    id: int
    name: str = None
    location: str = None
    time: str = None
    tags: str = None
    description: str = None
    good: int = None

# JSON 파일에서 읽어온 데이터 (예시)
item = {
    "id": 1,
    "name": "Spot 1",
    "location": "Seoul",
    "time": "12:00",
    "tags": "nature",
    "description": "A beautiful park",
    "good": 100
}

# **item을 사용하여 Spot 인스턴스 생성
spot = Spot(**item)

print(spot)
