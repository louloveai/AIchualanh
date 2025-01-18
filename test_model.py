import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Đường dẫn tới thư mục gốc
current_dir = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn đầy đủ
model_path = os.path.join(current_dir, "chatbot_model.pkl")
vectorizer_path = os.path.join(current_dir, "vectorizer.pkl")
chat_history_path = os.path.join(current_dir, "chat_history.csv")

# Kiểm tra và tải mô hình
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file mô hình tại {model_path}")
    exit(1)

# Tạo vectorizer
vectorizer = TfidfVectorizer()

# Kiểm tra và tải dữ liệu lịch sử chat
try:
    if not os.path.exists(chat_history_path):
        raise FileNotFoundError(f"Lỗi: Không tìm thấy file {chat_history_path}")
    chat_history = pd.read_csv(chat_history_path)

    if "message" not in chat_history.columns:
        raise ValueError("Lỗi: File chat_history.csv thiếu cột 'message'. Vui lòng kiểm tra lại file dữ liệu.")

    # Fit dữ liệu vào vectorizer
    vectorizer.fit(chat_history["message"])

except Exception as e:
    print(f"Lỗi khi xử lý dữ liệu lịch sử chat: {e}")
    exit(1)

# Kiểm tra mô hình trên dữ liệu thực tế
def test_model():
    while True:
        user_message = input("Nhập tin nhắn người dùng (gõ 'exit' để thoát): ")
        if user_message.lower() == "exit":
            break
        try:
            vectorized_message = vectorizer.transform([user_message])
            predicted_response = model.predict(vectorized_message)[0]
            print(f"AI phản hồi: {predicted_response}")
        except Exception as e:
            print(f"Lỗi khi xử lý tin nhắn: {e}")

if __name__ == "__main__":
    print("Bắt đầu kiểm tra mô hình...")
    test_model()

# Kiểm tra import joblib
logging.info("Đường dẫn thư mục 'models': ./models")
if os.path.exists("models/chatbot_model.pkl"):
    logging.info("File chatbot_model.pkl tồn tại.")
else:
    logging.error("File chatbot_model.pkl không tồn tại.")
if os.path.exists("models/vectorizer.pkl"):
    logging.info("File vectorizer.pkl tồn tại.")
else:
    logging.error("File vectorizer.pkl không tồn tại.")
