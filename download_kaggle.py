import os
import zipfile

# ====== Cấu hình Kaggle API ======
# Đặt đường dẫn Kaggle config, nơi chứa file kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "./config"

# ====== Tải dữ liệu từ Kaggle ======
def download_dataset():
    print("Đang tải dữ liệu từ Kaggle...")
    # Lệnh tải dữ liệu từ Kaggle
    result = os.system("kaggle datasets download -d iarunava/happydb -p ./data")
    if result != 0:
        print("Lỗi khi tải dữ liệu từ Kaggle. Kiểm tra Kaggle API key hoặc quyền truy cập.")
        return False
    return True

# ====== Giải nén file zip ======
def extract_zip():
    print("Đang giải nén dữ liệu...")
    zip_path = './data/happydb.zip'
    if not os.path.exists(zip_path):
        print("File zip không tồn tại. Dữ liệu chưa được tải về.")
        return False
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('./data')
    print("Giải nén hoàn tất!")
    return True

# ====== Chạy các bước ======
if __name__ == "__main__":
    # Đảm bảo thư mục ./data tồn tại
    if not os.path.exists('./data'):
        os.makedirs('./data')

    # Tải và giải nén dữ liệu
    if download_dataset():
        extract_zip()
    print("Hoàn thành!")
