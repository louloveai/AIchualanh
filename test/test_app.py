import pytest
from app import MentalHealthApp
from models.chat_model import ChatModel

def test_app_initialization():
    app = MentalHealthApp()
    assert app is not None

def test_response_generation():
    app = MentalHealthApp()
    response = app.get_response("Tôi cảm thấy buồn")
    assert response is not None
    assert isinstance(response, str)

def test_chat_model():
    model = ChatModel()
    emotion = model.detect_emotion("Tôi rất vui")
    assert emotion in ["joy", "sadness", "anger", "fear", "love", "surprise"] 
