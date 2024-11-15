from dotenv import load_dotenv
import os

load_dotenv()

class getConfig:
    
    def __init__(self):
        self.google_search_engine = os.getenv('GOOGLE_SEARCH_ENGINE')
        self.search_engine_id = os.getenv('SEARCH_ENGINE_ID')
    
    def get_config(self):
        return {
            'key':self.google_search_engine,
            'cx': self.search_engine_id,
            'num':3
            }
    


