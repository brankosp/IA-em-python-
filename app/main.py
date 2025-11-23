from fastapi import FastAPI
from app.schemas import RequestModel
from app.gemini_service import gerar_plano

app = FastAPI()

@app.get("/")
def root():
    return {"status":"ok", "message": "AI planner está online!"}

@app.post("/generate")
def generate_plan(data: RequestModel):
    return gerar_plano(
        data.goal,
        data.time_per_day,
        data.level,
        data.prefs
    )