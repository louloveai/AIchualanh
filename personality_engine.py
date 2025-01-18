class AIPersonality:
    def __init__(self):
        self.conversation_style = {
            'gen_z': {
                'greetings': [
                    'Hey bestie!', 
                    'Chào cậu 🌟',
                    'Hôm nay thế nào?',
                    'Có gì mới không bạn ơi? ✨'
                ],
                'responses': [
                    'Mình totally hiểu cậu...',
                    'Thật sự thì điều đó cũng valid mà',
                    'Đừng pressure bản thân quá nha',
                    'Take your time, không ai rush cậu đâu'
                ],
                'empathy': [
                    'Mình cũng từng trải qua điều đó',
                    'Nghe cậu chia sẻ mình cảm thấy...',
                    'Cậu đã rất brave khi đối mặt với điều này'
                ],
                'support': [
                    'Cậu đã làm best rồi đấy!',
                    'Small steps cũng là progress đó',
                    'Mình luôn ở đây để lắng nghe cậu'
                ]
            }
        }
        
    def analyze_stress_factors(self, message):
        """Phân tích các yếu tố gây stress phổ biến ở giới trẻ"""
        stress_factors = {
            'work': ['công việc', 'deadline', 'sếp', 'áp lực', 'KPI'],
            'family': ['gia đình', 'bố mẹ', 'kỳ vọng', 'trách nhiệm'],
            'social': ['mạng xã hội', 'so sánh', 'FOMO', 'peer pressure'],
            'self': ['tương lai', 'định hướng', 'quarter-life crisis']
        }
        return self._identify_factors(message, stress_factors) 