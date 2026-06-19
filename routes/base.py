from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")

async def welcome():
    app_name = os.getenv('APP_NAME', 'mini-rag')  # Default to 'mini-rag' if not set
    app_version = os.getenv('APP_VERSION', '0.0.1')  # Default to '0.0.1' if not set
    
    return {"message": f"Welcome all to the {app_name} {app_version}!"}


