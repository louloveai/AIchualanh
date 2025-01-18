class MoodTracker:
    def __init__(self):
        self.mood_scale = {
            1: "Rất tệ",
            2: "Không tốt",
            3: "Bình thường",
            4: "Tốt",
            5: "Rất tốt"
        }
        self.mood_history = {}
        
    def record_mood(self, user_id, mood_level, notes=""):
        if user_id not in self.mood_history:
            self.mood_history[user_id] = []
            
        self.mood_history[user_id].append({
            'date': datetime.now(),
            'level': mood_level,
            'notes': notes
        })
        
    def generate_mood_report(self, user_id, days=7):
        if user_id not in self.mood_history:
            return "Chưa có dữ liệu tâm trạng"
            
        recent_moods = self.mood_history[user_id][-days:]
        return self._analyze_mood_trends(recent_moods) 