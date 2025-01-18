import os
import pandas as pd


# Đường dẫn thư mục chứa các file CSV
current_dir = os.path.dirname(os.path.abspath(__file__))

# Lấy danh sách tất cả file CSV trong thư mục hiện tại
csv_files = [f for f in os.listdir(current_dir) if f.endswith(".csv")]

# Thêm các file cần kiểm tra cụ thể
additional_files = [
    "processed_data/X_train.csv",
    "processed_data/X_test.csv"
]

# Gộp danh sách file
all_files = csv_files + additional_files

# Kiểm tra từng file
for file_path in all_files:
    if not os.path.exists(file_path):
        print(f"File không tồn tại: {file_path}")
        continue
    try:
        df = pd.read_csv(file_path)
        if 'message' not in df.columns:
            print(f"Lỗi: Cột 'message' không tồn tại trong '{file_path}'")
        else:
            print(f"OK: Cột 'message' tồn tại trong '{file_path}'")
    except Exception as e:
        print(f"Lỗi khi đọc file '{file_path}': {e}")
