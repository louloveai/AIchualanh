import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
import logging

# Khởi tạo logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_processed_data():
    try:
        logging.info("Đọc dữ liệu từ các file CSV đã xử lý.")
        X_train = pd.read_csv("processed_data/X_train.csv")
        X_test = pd.read_csv("processed_data/X_test.csv")
        y_train = pd.read_csv("processed_data/y_train.csv")
        y_test = pd.read_csv("processed_data/y_test.csv")
        logging.info("Dữ liệu đã được tải thành công!")
        return X_train, X_test, y_train, y_test
    except FileNotFoundError as e:
        logging.error(f"Lỗi: Không tìm thấy file dữ liệu đã xử lý - {e}")
        raise
    except Exception as e:
        logging.error(f"Lỗi khi đọc dữ liệu: {e}")
        raise

def validate_data(X_train, X_test, y_train, y_test):
    try:
        if X_train.empty or X_test.empty or y_train.empty or y_test.empty:
            raise ValueError("Dữ liệu đầu vào trống.")
        if "message" not in X_train.columns or "message" not in X_test.columns:
            raise ValueError("Cột 'message' không tồn tại.")
        if X_train.isnull().values.any() or X_test.isnull().values.any():
            logging.warning("Dữ liệu chứa giá trị NaN. Đang tự động làm sạch.")
            X_train = X_train.fillna("")
            X_test = X_test.fillna("")
        logging.info("Dữ liệu hợp lệ!")
    except Exception as e:
        logging.error(f"Lỗi dữ liệu: {e}")
        raise

def preprocess_text_data(X_train, X_test):
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train["message"])
    X_test_tfidf = vectorizer.transform(X_test["message"])
    return X_train_tfidf, X_test_tfidf, vectorizer

def train_model(X_train, X_test, y_train, y_test):
    try:
        X_train_tfidf, X_test_tfidf, vectorizer = preprocess_text_data(X_train, X_test)
        y_train = y_train.values.ravel()
        y_test = y_test.values.ravel()
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train_tfidf, y_train)
        y_pred = model.predict(X_test_tfidf)
        accuracy = accuracy_score(y_test, y_pred)
        logging.info(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
        if not os.path.exists("models"):
            os.makedirs("models")
        joblib.dump(model, "models/chatbot_model.pkl")
        joblib.dump(vectorizer, "models/vectorizer.pkl")
        logging.info("Mô hình và vectorizer đã được lưu.")
    except Exception as e:
        logging.error(f"Lỗi trong quá trình huấn luyện mô hình: {e}")
        raise

if __name__ == "__main__":
    try:
        X_train, X_test, y_train, y_test = load_processed_data()
        validate_data(X_train, X_test, y_train, y_test)
        train_model(X_train, X_test, y_train, y_test)
    except Exception as e:
        logging.critical(f"Lỗi không xác định: {e}")
