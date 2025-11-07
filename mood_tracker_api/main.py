from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from typing import List, Annotated

app = FastAPI(
    title="Mood tracker API",
    description="Track your daily moods and analyze your emotional well-being",
)


class Mood(BaseModel):
    id: int
    mood: str
    mark: int
    note: str
    created_at: str


class MoodCreate(BaseModel):
    mood: str = Field(..., title="Describe your mood", min_length=1, max_length=10)
    mark: int = Field(..., title="Mark your mood from 1 to 10", ge=1, le=10)
    note: str = Field(..., title="Note your day", min_length=1, max_length=70)
    created_at: str = Field(..., title="Note date", min_length=1, max_length=10)


moods = [
    {
        "id": 1,
        "mood": "happy",
        "mark": 10,
        "note": "I have got a new job",
        "created_at": "2024-10-15",
    },
    {
        "id": 2,
        "mood": "sad",
        "mark": 4,
        "note": "I have no money",
        "created_at": "2024-08-28",
    },
    {
        "id": 3,
        "mood": "tired",
        "mark": 7,
        "note": "I had a lot of orders",
        "created_at": "2024-03-15",
    },
]


@app.get("/")
async def home():
    return {"message": "Mark your mood today"}


@app.get("/moods", response_model=List[Mood], summary="All notes of mood")
async def all_moods():
    return moods


@app.get("/mood/search/{id}", response_model=Mood)
async def get_mood(id: int):
    for mood in moods:
        if mood["id"] == id:
            return mood

    raise HTTPException(status_code=404, detail="Mood not found")


@app.post("/moods/add", response_model=Mood)
async def mood_add(mood_data: MoodCreate):

    if moods:
        new_mood_id = max(mood["id"] for mood in moods) + 1
    else:
        new_mood_id = 1

    new_mood = Mood(
        id=new_mood_id,
        mood=mood_data.mood,
        mark=mood_data.mark,
        note=mood_data.note,
        created_at=mood_data.created_at,
    )

    moods.append(new_mood.dict())

    return new_mood
