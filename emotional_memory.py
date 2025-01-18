from datetime import datetime
import json

class EmotionalMemory:
    def __init__(self):
        self.emotional_database = {}  # Lưu trữ theo user_id
        
    def store_emotion(self, user_id, message, emotion_data):
        """Lưu trữ cảm xúc và ngữ cảnh"""
        timestamp = datetime.now()
        
        if user_id not in self.emotional_database:
            self.emotional_database[user_id] = []
            
        emotion_entry = {
            'timestamp': timestamp,
            'emotion': emotion_data['emotion'],  # vd: buồn, vui, giận...
            'intensity': emotion_data['intensity'],  # mức độ cảm xúc (1-10)
            'context': self._extract_context(message),  # nguyên nhân
            'triggers': self._identify_triggers(message),  # yếu tố kích hoạt
            'related_people': self._extract_people(message),  # người liên quan
            'raw_message': message
        }
        
        self.emotional_database[user_id].append(emotion_entry)
        
    def _extract_context(self, message):
        """Trích xuất ngữ cảnh từ tin nhắn"""
        context_keywords = {
            'family': ['mẹ', 'bố', 'gia đình', 'nhà'],
            'work': ['công việc', 'sếp', 'công ty', 'deadline'],
            'relationship': ['người yêu', 'bạn trai', 'bạn gái', 'tình cảm'],
            'study': ['học', 'thi', 'trường', 'bài tập']
        }
        
        found_context = []
        for context, keywords in context_keywords.items():
            if any(keyword in message.lower() for keyword in keywords):
                found_context.append(context)
                
        return found_context
        
    def get_emotional_history(self, user_id, days=30):
        """Lấy lịch sử cảm xúc của người dùng"""
        if user_id not in self.emotional_database:
            return []
            
        history = self.emotional_database[user_id]
        return sorted(history, key=lambda x: x['timestamp'], reverse=True)
        
    def analyze_patterns(self, user_id):
        """Phân tích mẫu cảm xúc"""
        history = self.get_emotional_history(user_id)
        
        return {
            'common_emotions': self._get_common_emotions(history),
            'frequent_triggers': self._get_frequent_triggers(history),
            'emotional_trends': self._analyze_trends(history),
            'related_people_impact': self._analyze_people_impact(history)
        }
        
    def generate_insight(self, user_id):
        """Tạo insight từ dữ liệu cảm xúc"""
        patterns = self.analyze_patterns(user_id)
        
        return {
            'summary': f"Trong 30 ngày qua, bạn thường cảm thấy {patterns['common_emotions'][0]} nhất",
            'triggers': f"Yếu tố thường gây ảnh hưởng đến cảm xúc của bạn: {', '.join(patterns['frequent_triggers'][:3])}",
            'suggestion': self._generate_suggestion(patterns)
        } 