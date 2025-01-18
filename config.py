import os
from dotenv import load_dotenv
from transformers import pipeline
import streamlit_authenticator as stauth
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from functools import wraps
import time
import logging
from datetime import datetime

class Config:
    def __init__(self):
        load_dotenv()
        
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("Thiếu biến môi trường API_KEY")
        self.model_path = os.getenv("MODEL_PATH", "models/chatbot_model.pkl")
        self.max_tokens = int(os.getenv("MAX_TOKENS", 100))
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))

class EmotionDetector:
    def __init__(self):
        self.classifier = pipeline("text-classification", 
                                 model="bhadresh-savani/distilbert-base-uncased-emotion")
    
    def detect_emotion(self, text):
        result = self.classifier(text)
        return result[0]['label']

def setup_auth():
    authenticator = stauth.Authenticate(
        credentials,
        cookie_name='mental_health_app',
        key='auth_key',
        cookie_expiry_days=30
    )
    return authenticator

Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = 'chat_history'
    id = Column(String, primary_key=True)
    user_id = Column(String)
    message = Column(String)
    emotion = Column(String)
    timestamp = Column(DateTime)

def setup_custom_theme():
    st.markdown("""
        <style>
        .stApp {
            background: #ffffff;
            color: #000000;
        }
        .chat-message {
            padding: 0.8rem;
            border-radius: 8px;
            margin: 0.8rem 0;
            border: 1px solid #e0e0e0;
            background: #fafafa;
        }
        .stButton button {
            background: #000000;
            color: #ffffff;
            border: none;
        }
        .stTextInput input {
            border: 1px solid #e0e0e0;
            background: #ffffff;
        }
        </style>
    """, unsafe_allow_html=True)

def rate_limit(limit=5, window=60):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls_in_window = [call for call in calls if call > now - window]
            if len(calls_in_window) >= limit:
                raise Exception("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def setup_logging():
    logging.basicConfig(
        filename=f'logs/app_{datetime.now().strftime("%Y%m%d")}.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

class MentalHealthBot:
    """
    A comprehensive mental health support chatbot.
    
    Features:
    - Emotion detection
    - Multi-language support
    - Voice integration
    - User progress tracking
    
    Methods:
    - process_message: Processes user input and returns appropriate response
    - track_emotion: Tracks user's emotional state over time
    - generate_report: Generates user progress report
    """
