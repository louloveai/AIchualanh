class DataSynthesizer:
    def __init__(self):
        self.base_patterns = load_patterns()
        
    def generate_variations(self, pattern):
        """Tạo các biến thể của pattern"""
        variations = []
        # Thay đổi chủ ngữ
        for subject in self.base_patterns['subjects']:
            # Thay đổi hành động
            for action in self.base_patterns['actions']:
                # Thay đổi cảm xúc
                for emotion in self.base_patterns['emotions']:
                    new_variation = pattern.format(
                        subject=subject,
                        action=action,
                        emotion=emotion
                    )
                    variations.append(new_variation)
        return variations 
