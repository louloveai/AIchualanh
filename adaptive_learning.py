class AdaptiveLearningSystem:
    def __init__(self):
        self.learning_metrics = {
            'response_effectiveness': {},  # Đánh giá hiệu quả phản hồi
            'user_satisfaction': {},      # Mức độ hài lòng
            'conversation_flow': {},      # Độ tự nhiên của cuộc trò chuyện
            'emotional_impact': {}        # Tác động đến cảm xúc người dùng
        }
        
    def learn_from_interaction(self, interaction_data):
        """Học và cải thiện từ mỗi tương tác"""
        self._analyze_response_effectiveness(interaction_data)
        self._update_conversation_patterns(interaction_data)
        self._improve_emotional_understanding(interaction_data)
        
        return self._generate_improvement_metrics()
        
    def _analyze_response_effectiveness(self, data):
        """Phân tích và đánh giá hiệu quả phản hồi"""
        user_feedback = data.get('user_feedback')
        conversation_length = data.get('conversation_length')
        emotional_change = data.get('emotional_change')
        
        effectiveness_score = self._calculate_effectiveness(
            user_feedback,
            conversation_length,
            emotional_change
        )
        
        self.learning_metrics['response_effectiveness'].update({
            data['conversation_id']: effectiveness_score
        }) 