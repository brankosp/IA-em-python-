from pydantic import BaseModel
from typing import List

class Step(BaseModel):
    step_number: int
    title: str
    duration_min: int
    details: str

class Plan(BaseModel):
    goal: str
    estimated_total_minutes: int
    steps: List[Step]

class RequestModel(BaseModel):
    goal: str
    time_per_day: int
    level: str = "iniciante"
    prefs: str = ""