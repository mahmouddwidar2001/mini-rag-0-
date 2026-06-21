from controllers.BaseControllers import BaseControllers
from fastapi import UploadFile

class DataController(BaseControllers):
    def __init__(self):
        super().__init__()
        self.filescale = 1024 * 1024  # 1 MB in bytes

    def validate_upload_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.app_settings.FILE_MAX_SIZE * self.filescale:
            return False
        return True

    
  

