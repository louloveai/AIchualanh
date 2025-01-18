import os
import pandas as pd
from sklearn.model_selection import train_test_split
import re

# ====== Đường dẫn file ======
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "data.csv")

# ====== Đọc dữ liệu ======
def load_and_validate_data(file_path, required_columns):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} không tồn tại.")

    try:
        df = pd.read_csv(file_path)
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Dữ liệu thiếu các cột bắt buộc: {missing_cols}")
        
        df = df.dropna(how="all").drop_duplicates()  # Loại bỏ hàng trống và trùng lặp
        print(f"Dữ liệu sau xử lý: {df.shape[0]} hàng.")
        return df
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc hoặc kiểm tra dữ liệu: {e}")

# ====== Làm sạch dữ liệu ======
def clean_text_column(df, column):
    if column not in df.columns:
        raise ValueError(f"Cột '{column}' không tồn tại trong dữ liệu.")
    
    def preprocess_text(text):
        text = str(text).lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text.strip()
    
    df[column] = df[column].apply(preprocess_text)
    print("Đã làm sạch dữ liệu.")
    return df

# ====== Chia dữ liệu ======
def split_data(df, feature_column, label_column, test_size=0.2, random_state=42):
    if feature_column not in df.columns or label_column not in df.columns:
        raise ValueError(f"Cột '{feature_column}' hoặc '{label_column}' không tồn tại.")
    
    X = df[feature_column]
    y = df[label_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"Dữ liệu chia thành công: Train ({len(X_train)}), Test ({len(X_test)})")
    return X_train, X_test, y_train, y_test

# ====== Lưu dữ liệu ======
def save_data(X_train, X_test, y_train, y_test, output_dir="processed_data"):
    os.makedirs(output_dir, exist_ok=True)
    pd.DataFrame(X_train).to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    pd.DataFrame(X_test).to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
    pd.DataFrame(y_train).to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    pd.DataFrame(y_test).to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
    print(f"Dữ liệu đã lưu vào thư mục '{output_dir}'.")

# ====== Chạy chương trình chính ======
if __name__ == "__main__":
    try:
        # Các cột yêu cầu trong dữ liệu
        required_columns = ["message", "label"]

        # Đọc và kiểm tra dữ liệu
        data = load_and_validate_data(data_path, required_columns)

        # Làm sạch dữ liệu
        data = clean_text_column(data, "message")

        # Chia dữ liệu
        X_train, X_test, y_train, y_test = split_data(data, "message", "label")

        # Lưu dữ liệu
        save_data(X_train, X_test, y_train, y_test)

        print("Quá trình xử lý dữ liệu hoàn tất!")
    except Exception as e:
        print(f"Lỗi trong quá trình xử lý: {e}")
