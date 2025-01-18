class ValidationHandler:
    def __init__(self):
        self.required_fields = {
            'emotion': ['type', 'intensity', 'duration'],
            'user': ['id', 'context', 'history'],
            'session': ['id', 'start_time', 'status']
        }

    def validate_input(self, data, data_type):
        if data_type not in self.required_fields:
            raise ValueError(f"Unknown data type: {data_type}")
            
        for field in self.required_fields[data_type]:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
            
        return True

    def validate_emotion(self, emotion_data):
        try:
            self.validate_input(emotion_data, 'emotion')
            if not (0 <= emotion_data['intensity'] <= 10):
                raise ValueError("Intensity must be between 0 and 10")
        except Exception as e:
            raise ValueError(f"Emotion validation failed: {str(e)}") 