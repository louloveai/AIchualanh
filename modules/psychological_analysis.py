class PsychologicalAnalysis:
    def __init__(self):
        self.analysis_tools = {
            "cảm_xúc": {
                "nhận_diện": ["vui", "buồn", "giận", "sợ", "lo âu"],
                "mức_độ": range(1, 11),  # 1-10
                "tần_suất": ["thỉnh thoảng", "thường xuyên", "liên tục"]
            },
            "hành_vi": {
                "thói_quen": ["ăn uống", "ngủ nghỉ", "vận động"],
                "tương_tác": ["gia đình", "bạn bè", "đồng nghiệp"],
                "thay_đổi": ["tích cực", "tiêu cực", "không đổi"]
            },
            "suy_nghĩ": {
                "mô_hình": ["tích cực", "tiêu cực", "trung tính"],
                "tần_suất": ["thỉnh thoảng", "thường xuyên", "liên tục"],
                "ảnh_hưởng": ["nhẹ", "trung bình", "nặng"]
            }
        }