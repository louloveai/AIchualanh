class SmartResponseSystem:
    def __init__(self):
        self.response_patterns = {
            'validation': [
                "Cảm xúc của cậu hoàn toàn valid",
                "Mình hiểu vì sao cậu cảm thấy vậy",
                "Điều cậu đang trải qua không dễ dàng gì"
            ],
            'empowerment': [
                "Cậu mạnh mẽ hơn cậu nghĩ đấy",
                "Mỗi bước nhỏ đều đáng trân trọng",
                "Hãy tự hào về những gì cậu đã vượt qua"
            ],
            'practical_advice': [
                "Hay là mình thử journaling?",
                "Cậu đã thử phương pháp 5-4-3-2-1 chưa?",
                "Đôi khi một playlist lofi cũng giúp tâm trạng tốt hơn đấy"
            ]
        }
        
    def generate_personalized_response(self, user_message, user_profile):
        """Tạo phản hồi phù hợp với phong cách và nhu cầu của người dùng"""
        emotion = self.analyze_emotion(user_message)
        context = self.get_conversation_context(user_profile)
        return self._craft_response(emotion, context) 