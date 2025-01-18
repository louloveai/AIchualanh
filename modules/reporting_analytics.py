class ReportingAnalytics:
    def __init__(self):
        self.analytics_tools = {
            "báo_cáo_người_dùng": {
                "tương_tác": ["thời gian", "tần suất", "mức độ"],
                "tiến_triển": ["cải thiện", "ổn định", "cần hỗ trợ"],
                "phản_hồi": ["đánh giá", "góp ý", "yêu cầu"]
            },
            "phân_tích_xu_hướng": {
                "cá_nhân": ["hành vi", "cảm xúc", "tương tác"],
                "cộng_đồng": ["chủ đề hot", "vấn đề phổ biến"],
                "hiệu_quả": ["tỷ lệ cải thiện", "thời gian phục hồi"]
            }
        } 