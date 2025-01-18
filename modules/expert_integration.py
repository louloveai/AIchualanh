class ExpertIntegration:
    def __init__(self):
        self.expert_network = {
            "chuyên_gia": {
                "tâm_lý": ["tư vấn", "trị liệu", "coaching"],
                "tâm_thần": ["bác sĩ", "chuyên gia", "nhà trị liệu"],
                "hỗ_trợ": ["nhân viên xã hội", "cố vấn", "mentor"]
            },
            "kết_nối": {
                "trực_tiếp": ["cuộc hẹn", "tư vấn online", "hotline"],
                "gián_tiếp": ["email", "chat", "forum"]
            },
            "khẩn_cấp": {
                "đường_dây_nóng": ["24/7", "miễn phí", "bảo mật"],
                "can_thiệp": ["khủng hoảng", "cấp cứu", "hỗ trợ"]
            }
        } 
