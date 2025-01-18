import random

class ResponseGenerator:
    def __init__(self):
        self.responses = {
            "joy": [
                "Thật vui khi thấy bạn hạnh phúc! Hãy chia sẻ niềm vui này nhé.",
                "Cảm xúc tích cực sẽ giúp tăng endorphin - hormone hạnh phúc trong cơ thể bạn."
            ],
            "sadness": [
                "Tôi hiểu cảm giác buồn bã của bạn. Hãy chia sẻ để tôi lắng nghe nhé.",
                "Đôi khi nói ra nỗi buồn sẽ giúp bạn cảm thấy nhẹ nhàng hơn."
            ],
            "neutral": [
                "Bạn đang cảm thấy thế nào? Hãy chia sẻ thêm nhé.",
                "Tôi luôn ở đây để lắng nghe bạn."
            ]
        }

    def get_response(self, emotion: str) -> str:
        return random.choice(self.responses.get(emotion, self.responses["neutral"])) 
