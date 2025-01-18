from .file_handler import FileHandler
from .validation_handler import ValidationHandler

class DataLoader:
    def __init__(self):
        self.file_handler = FileHandler()
        self.validator = ValidationHandler()
        self.loaded_data = {}

    def load_emotions(self):
        data = self.file_handler.load_json('emotion.json')
        self.loaded_data['emotions'] = data
        return data

    def load_patterns(self):
        data = self.file_handler.load_json('conversation_patterns.json')
        self.loaded_data['patterns'] = data
        return data

    def load_all(self):
        try:
            self.load_emotions()
            self.load_patterns()
            return True
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}") 
