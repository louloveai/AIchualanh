from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob
import joblib
import os
from flask import Flask, request, jsonify, render_template
import pandas as pd
import logging

# Khởi tạo Flask app
app = Flask(__name__)

# Thiết lập logging
logging.basicConfig(
    filename="error.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Ứng dụng Flask đã khởi chạy.")

# Lấy đường dẫn tuyệt đối tới file
current_dir = os.path.dirname(os.path.abspath(__file__))
lda_model_path = os.path.join(current_dir, "lda_model.pkl")
vectorizer_path = os.path.join(current_dir, "vectorizer.pkl")
data_path = os.path.join(current_dir, "data.csv")

# ===== Kiểm tra sự tồn tại của file =====
def check_file_existence(file_path, file_description):
    if os.path.exists(file_path):
        logging.info(f"{file_description} tồn tại: {file_path}")
    else:
        logging.error(f"{file_description} không tồn tại: {file_path}")
        raise FileNotFoundError(f"{file_description} không tồn tại.")

check_file_existence(lda_model_path, "Mô hình LDA")
check_file_existence(vectorizer_path, "Vectorizer")
check_file_existence(data_path, "Dữ liệu CSV")

# ===== Kiểm tra và tải mô hình =====
def check_and_load_models():
    """
    Kiểm tra và tải mô hình LDA và Vectorizer.
    """
    try:
        lda_model = joblib.load(lda_model_path)
        vectorizer = joblib.load(vectorizer_path)
        logging.info("Mô hình và vectorizer đã được tải thành công.")
        return lda_model, vectorizer
    except Exception as e:
        logging.error(f"Lỗi khi tải mô hình hoặc vectorizer: {e}")
        raise ValueError("Không thể tải mô hình hoặc vectorizer.")

lda_model, vectorizer = check_and_load_models()

# ===== Tải và kiểm tra dữ liệu =====
def load_and_validate_data(file_path, required_columns):
    """
    Tải và kiểm tra dữ liệu từ file CSV.
    """
    try:
        df = pd.read_csv(file_path)
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Dữ liệu thiếu các cột bắt buộc: {missing_cols}")
        df = df.dropna(how="all").drop_duplicates()
        logging.info(f"Dữ liệu đã được tải thành công: {file_path}")
        return df
    except Exception as e:
        logging.error(f"Lỗi khi tải dữ liệu: {e}")
        raise

required_columns = ["message", "label"]
data = load_and_validate_data(data_path, required_columns)

# ===== Gợi ý chủ đề =====
def suggest_topics(user_message):
    """
    Gợi ý chủ đề dựa trên tin nhắn của người dùng.
    """
    try:
        if not user_message.strip():
            raise ValueError("Tin nhắn đầu vào trống.")
        tfidf_vector = vectorizer.transform([user_message])
        topic_distribution = lda_model.transform(tfidf_vector)
        top_topic = topic_distribution.argmax()
        return f"Chủ đề gợi ý: {top_topic}"
    except Exception as e:
        logging.error(f"Lỗi khi phân tích chủ đề: {e}")
        return "Không thể gợi ý chủ đề."

# ===== Phân tích cảm xúc =====
def analyze_emotion_with_textblob(message):
    """
    Phân tích cảm xúc bằng TextBlob.
    """
    try:
        analysis = TextBlob(message)
        polarity = analysis.sentiment.polarity
        if polarity < -0.3:
            return "negative"
        elif polarity > 0.3:
            return "positive"
        return "neutral"
    except Exception as e:
        logging.error(f"Lỗi khi phân tích cảm xúc: {e}")
        return "unknown"

# ===== API Chat =====
@app.route("/chat", methods=["POST"])
def chat():
    """
    API xử lý tin nhắn từ người dùng.
    """
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"response": "Tin nhắn của bạn trống. Vui lòng nhập nội dung."}), 400
        suggestion = suggest_topics(user_message)
        return jsonify({"response": f"Tôi gợi ý bạn quan tâm đến: {suggestion}"})
    except Exception as e:
        logging.error(f"Lỗi trong API Chat: {e}")
        return jsonify({"response": "Có lỗi xảy ra. Vui lòng thử lại sau."}), 500

# ===== API Phân tích cảm xúc =====
@app.route("/analyze", methods=["POST"])
def analyze_emotion():
    """
    API phân tích cảm xúc.
    """
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"response": "Tin nhắn của bạn trống. Vui lòng nhập nội dung."}), 400
        emotion = analyze_emotion_with_textblob(user_message)
        return jsonify({"response": f"Tin nhắn của bạn được đánh giá là: {emotion}"})
    except Exception as e:
        logging.error(f"Lỗi trong API Phân tích cảm xúc: {e}")
        return jsonify({"response": "Có lỗi xảy ra. Vui lòng thử lại sau."}), 500

# ===== Trang chính =====
@app.route("/")
def home():
    """
    Trang chính render template index.html.
    """
    emotion_log = {"2025-01-07": ["happy", "calm"], "2025-01-06": ["stressed"]}
    return render_template("index.html", emotion_log=emotion_log)

# ===== Chạy ứng dụng =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
