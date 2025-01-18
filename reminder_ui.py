class ReminderUI:
    def __init__(self):
        self.st = st
        
    def show_reminder_settings(self):
        self.st.sidebar.header("⏰ Cài đặt nhắc nhở")
        
        # Cài đặt check-in
        self.st.sidebar.subheader("Check-in hàng ngày")
        checkin_time = self.st.sidebar.time_input("Thời gian check-in", datetime.strptime("09:00", "%H:%M"))
        
        # Cài đặt mindfulness
        self.st.sidebar.subheader("Lịch thực hành mindfulness")
        mindfulness_frequency = self.st.sidebar.number_input("Số lần thực hành mỗi ngày", 1, 5, 3)
        
        # Theo dõi tâm trạng
        self.st.sidebar.subheader("Theo dõi tâm trạng")
        mood_tracking = self.st.sidebar.checkbox("Bật theo dõi tâm trạng hàng ngày")
        
        return {
            'checkin_time': checkin_time,
            'mindfulness_frequency': mindfulness_frequency,
            'mood_tracking': mood_tracking
        } 