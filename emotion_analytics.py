class EmotionDataAnalytics:
    def __init__(self, emotional_memory):
        self.emotional_memory = emotional_memory
        self.emotion_colors = {
            'vui': '#FFD700',      # Màu vàng
            'buồn': '#4682B4',     # Màu xanh dương
            'giận': '#DC143C',     # Màu đỏ
            'lo lắng': '#9370DB',  # Màu tím
            'bình yên': '#98FB98'  # Màu xanh lá
        }

    def get_emotion_data(self, user_id, time_range='month'):
        """Lấy dữ liệu cảm xúc theo thời gian"""
        history = self.emotional_memory.get_emotional_history(user_id)
        
        emotion_data = {
            'timeline': self._format_timeline_data(history),
            'statistics': self._calculate_statistics(history),
            'patterns': self._identify_patterns(history),
            'insights': self._generate_insights(history)
        }
        
        return emotion_data
        
    def _format_timeline_data(self, history):
        """Format dữ liệu timeline"""
        timeline = []
        for entry in history:
            timeline_entry = {
                'date': entry['timestamp'].strftime("%d/%m/%Y"),
                'time': entry['timestamp'].strftime("%H:%M"),
                'emotion': entry['emotion'],
                'context': entry['context'],
                'intensity': entry['intensity'],
                'color': self.emotion_colors.get(entry['emotion'], '#808080'),
                'description': f"{entry['emotion'].title()} - {entry['raw_message']}"
            }
            timeline.append(timeline_entry)
        return timeline

    def _calculate_statistics(self, history):
        """Tính toán thống kê cảm xúc"""
        emotion_counts = {}
        triggers = {}
        
        for entry in history:
            # Đếm số lần xuất hiện của mỗi cảm xúc
            emotion = entry['emotion']
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
            
            # Đếm triggers phổ biến
            for trigger in entry['triggers']:
                triggers[trigger] = triggers.get(trigger, 0) + 1
                
        return {
            'emotion_distribution': emotion_counts,
            'common_triggers': triggers,
            'total_entries': len(history)
        }

    def _identify_patterns(self, history):
        """Nhận diện pattern cảm xúc"""
        return {
            'daily_patterns': self._analyze_daily_patterns(history),
            'weekly_patterns': self._analyze_weekly_patterns(history),
            'trigger_patterns': self._analyze_trigger_patterns(history)
        }

    def _generate_insights(self, history):
        """Tạo insights từ dữ liệu"""
        stats = self._calculate_statistics(history)
        patterns = self._identify_patterns(history)
        
        # Tìm cảm xúc phổ biến nhất
        most_common_emotion = max(stats['emotion_distribution'].items(), 
                                key=lambda x: x[1])[0]
                                
        # Tìm trigger phổ biến nhất
        most_common_trigger = max(stats['common_triggers'].items(), 
                                key=lambda x: x[1])[0]
                                
        return {
            'summary': f"Bạn thường cảm thấy {most_common_emotion} nhất trong thời gian qua",
            'trigger_insight': f"Yếu tố '{most_common_trigger}' thường ảnh hưởng đến cảm xúc của bạn",
            'suggestions': self._generate_suggestions(most_common_emotion, patterns)
        } 