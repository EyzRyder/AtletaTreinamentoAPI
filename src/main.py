from fastapi import FastAPI
from src.routers import api_router


app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
