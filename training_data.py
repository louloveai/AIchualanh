class TrainingDataset:
    def __init__(self):
        self.data_sources = {
            'conversation_samples': {
                'therapeutic_dialogues': [],  # Các cuộc đối thoại trị liệu mẫu
                'counseling_sessions': [],    # Phiên tư vấn tâm lý
                'support_conversations': []    # Hội thoại hỗ trợ tinh thần
            },
            'emotional_patterns': {
                'trigger_response': [],       # Cặp trigger-phản ứng cảm xúc
                'coping_strategies': [],      # Chiến lược đối phó
                'emotional_transitions': []    # Quá trình chuyển đổi cảm xúc
            },
            'psychological_cases': {
                'case_studies': [],          # Cases nghiên cứu tâm lý
                'treatment_approaches': [],   # Phương pháp điều trị
                'outcome_analysis': []        # Phân tích kết quả
            }
        }
        
    def load_essential_data(self):
        """Các nguồn dữ liệu cần thiết tối thiểu"""
        return {
            'min_conversations': 1000,    # Ít nhất 1000 cuộc hội thoại
            'min_emotions': 500,          # 500 mẫu cho mỗi loại cảm xúc
            'min_cases': 200,             # 200 cases nghiên cứu
            'min_techniques': 50          # 50 kỹ thuật trị liệu
        } 