class PatternGenerator:
    def __init__(self):
        self.nlp = spacy.load('vi_core_news_lg')  # Sử dụng thư viện NLP
        
    def generate_templates(self, raw_conversations):
        """Tự động tạo templates từ dữ liệu thô"""
        templates = []
        for conv in raw_conversations:
            # Phát hiện entities (người, hành động, cảm xúc)
            entities = self.extract_entities(conv)
            # Tạo template thay thế entities bằng placeholders
            template = self.create_template(conv, entities)
            templates.append(template)
        return templates 
