from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class ChatModel:
    def __init__(self):
        try:
            self.emotion_classifier = pipeline(
                "text-classification",
                model="bhadresh-savani/distilbert-base-uncased-emotion"
            )
        except Exception as e:
            logger.error(f"Error initializing model: {e}")
            raise

    def detect_emotion(self, text):
        try:
            for _ in range(3):
                try:
                    result = self.emotion_classifier(text)
                    return result[0]['label']
                except Exception:
                    continue
            return "neutral"
        except Exception as e:
            logger.error(f"Lỗi khi phát hiện cảm xúc: {e}")
            return "neutral"

    def generate_response(self, text, emotion):
        # Add your response generation logic here
        pass 
