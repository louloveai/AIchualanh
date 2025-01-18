import os

# Đặt đường dẫn đến thư mục chứa file kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "./config"

# Kiểm tra xem Kaggle API hoạt động không
try:
    os.system("kaggle datasets list")
    print("Kaggle API hoạt động!")
except Exception as e:
    print(f"Lỗi khi kết nối Kaggle API: {e}") 
