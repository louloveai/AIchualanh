class ProgressTracking:
    def __init__(self):
        self.tracking_metrics = {
            "nhật_ký_tâm_trạng": {
                "thời_gian": "timestamp",
                "cảm_xúc": "emotion_type",
                "mức_độ": "intensity",
                "ghi_chú": "notes"
            },
            "mục_tiêu": {
                "ngắn_hạn": ["hàng ngày", "hàng tuần"],
                "trung_hạn": ["hàng tháng", "hàng quý"],
                "dài_hạn": ["6 tháng", "1 năm"]
            },
            "đánh_giá_tiến_bộ": {
                "chỉ_số": ["tâm trạng", "giấc ngủ", "năng lượng"],
                "xu_hướng": ["cải thiện", "ổn định", "suy giảm"],
                "giai_đoạn": ["bắt đầu", "giữa kỳ", "kết thúc"]
            }
        } 