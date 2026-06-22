from fastapi import FastAPI, APIRouter, Depends, UploadFile, status, Request
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController
import os
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1,data"],
)



@data_router.post("/upload/{project_id}")
async def upload_data(request: Request, project_id: int, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):

    # validate the file properties
    data_controller = DataController()

    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

