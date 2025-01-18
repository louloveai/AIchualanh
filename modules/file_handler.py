import json
import os

class FileHandler:
    def __init__(self):
        self.base_path = 'data/raw/'

    def load_json(self, filename):
        try:
            with open(os.path.join(self.base_path, filename), 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading {filename}: {str(e)}")

    def save_json(self, data, filename):
        try:
            with open(os.path.join(self.base_path, filename), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Error saving {filename}: {str(e)}") 