class UserAnalytics:
    def __init__(self):
        self.metrics = {
            'user_engagement': {
                'chat_frequency': {},     # Tần suất sử dụng
                'session_length': {},     # Thời gian mỗi phiên
                'return_rate': {},        # Tỷ lệ quay lại
                'feature_usage': {}       # Mức độ sử dụng các tính năng
            },
            'ai_effectiveness': {
                'response_ratings': {},    # Đánh giá phản hồi
                'problem_solved': {},      # Vấn đề được giải quyết
                'user_mood_improvement': {} # Cải thiện tâm trạng
            },
            'user_demographics': {
                'age_groups': {},         # Phân bố độ tuổi
                'locations': {},          # Vị trí địa lý
                'usage_times': {}         # Thời điểm sử dụng
            },
            'conversation_data': {
                'common_topics': {},      # Chủ đề phổ biến
                'emotional_patterns': {},  # Mẫu cảm xúc
                'session_duration': {}    # Thời lượng trò chuyện
            }
        }
    
    def collect_user_data(self, user_id, interaction_data):
        """Thu thập dữ liệu tương tác của người dùng"""
        timestamp = datetime.now()
        
        # Cập nhật metrics người dùng
        self._update_engagement_metrics(user_id, timestamp, interaction_data)
        self._update_effectiveness_metrics(user_id, interaction_data)
        self._update_demographic_data(user_id, interaction_data)
        self._update_conversation_metrics(user_id, interaction_data)
        
    def export_analytics_data(self, start_date=None, end_date=None):
        """Xuất dữ liệu phân tích"""
        return {
            'user_metrics': self._compile_user_metrics(start_date, end_date),
            'ai_performance': self._compile_ai_metrics(start_date, end_date),
            'user_segments': self._compile_demographic_data(start_date, end_date),
            'conversation_analysis': self._compile_conversation_data(start_date, end_date)
        } 