from fastapi import FastAPI, APIRouter ,Depends , UploadFile
from helpers.config import get_settings,settings
from controllers import DataController
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1,data"],
)


@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile
                    ,app_settings : settings = Depends(get_settings)):

    # validate file type and size
    is_valid = DataController().validate_upload_file(file=file)
    return {"valid": is_valid, "project_id": project_id}
