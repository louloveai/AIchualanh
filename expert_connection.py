class ExpertSystem:
    def __init__(self):
        self.warning_signs = [
            "tự tử", "trầm cảm nặng", "hoảng loạn",
            "không muốn sống", "tổn thương nghiêm trọng"
        ]
        
    def check_for_warning_signs(self, message):
        """Kiểm tra các dấu hiệu cần sự trợ giúp chuyên môn"""
        for sign in self.warning_signs:
            if sign in message.lower():
                return True
        return False
        
    def suggest_expert_help(self):
        return {
            "message": "Tôi nghĩ bạn nên tham khảo ý kiến chuyên gia. Đây là một số đường dây hỗ trợ:",
            "hotlines": [
                "Đường dây nóng tư vấn tâm lý: xxxx",
                "Trung tâm hỗ trợ sức khỏe tinh thần: yyyy"
            ]
        } 