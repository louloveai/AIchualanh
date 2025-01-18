class NotificationService:
    def __init__(self):
        self.notification_methods = {
            'web': self._send_web_notification,
            'email': self._send_email_notification,
            'mobile': self._send_mobile_notification
        }
    
    def send_reminder(self, user_id, reminder_type, message):
        user_preferences = self._get_user_preferences(user_id)
        notification_method = user_preferences.get('notification_method', 'web')
        
        return self.notification_methods[notification_method](user_id, message)
        
    def _send_web_notification(self, user_id, message):
        st.toast(message)
        return True 