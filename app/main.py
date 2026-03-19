from fastapi import FastAPI
from app.api.routes import router
app = FastAPI(
    title="Trade Opportunities API",
    description="AI-powered sector analysis for Indian markets",
    version="1.0")

app.include_router(router)
