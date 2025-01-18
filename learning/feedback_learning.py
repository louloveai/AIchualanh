class FeedbackLearner:
    def __init__(self):
        self.response_ratings = {}
        
    def learn_from_feedback(self, user_response, ai_response, rating):
        """Học từ phản hồi của người dùng"""
        if rating > 4:  # Nếu phản hồi tốt
            # Tự động tạo thêm variations của pattern này
            new_patterns = self.generate_variations(user_response)
            # Cập nhật vào database
            self.update_training_data(new_patterns) 
