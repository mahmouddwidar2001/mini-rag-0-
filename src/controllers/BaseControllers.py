from helpers.config import settings, get_settings

class BaseControllers:
    
    def __init__(self):
        self.app_settings = get_settings()
        
