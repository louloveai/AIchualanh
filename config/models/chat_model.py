class ChatModel:
    def __init__(self):
        try:
            self.emotion_classifier = pipeline(
                "text-classification",
                model="bhadresh-savani/distilbert-base-uncased-emotion",
                device=-1  # Thêm để sử dụng CPU nếu không có GPU
            )
            self.translator = GoogleTranslator(source='vi', target='en')  # Thêm translator
        except Exception as e:
            logger.error(f"Lỗi khởi tạo mô hình: {e}")
            raise

    def detect_emotion(self, text):
        try:
            # Dịch văn bản tiếng Việt sang tiếng Anh trước
            english_text = self.translator.translate(text)
            result = self.emotion_classifier(english_text)
            return result[0]['label']
        except Exception as e:
            logger.error(f"Lỗi phát hiện cảm xúc: {e}")
            return "neutral"  # Trả về giá trị an toàn 
