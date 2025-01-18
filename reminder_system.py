class ReminderSystem:
    def __init__(self):
        self.reminders = {
            'daily_checkin': {
                'time': '09:00',
                'message': 'Hãy chia sẻ cảm xúc của bạn hôm nay nhé!'
            },
            'mindfulness': {
                'times': ['07:00', '12:00', '19:00'],
                'messages': [
                    'Đã đến giờ thực hành thở sâu',
                    'Dành 5 phút để thiền định nhé',
                    'Hãy tập trung vào giây phút hiện tại'
                ]
            },
            'mood_tracking': {
                'time': '20:00',
                'message': 'Hãy đánh giá tâm trạng của bạn hôm nay'
            }
        }
        self.user_preferences = {}
        
    def set_user_preferences(self, user_id, preferences):
        self.user_preferences[user_id] = preferences
        
    def get_daily_schedule(self, user_id):
        if user_id not in self.user_preferences:
            return self.reminders
        return self._customize_schedule(user_id) 