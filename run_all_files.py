import os
import subprocess

# Đường dẫn tới thư mục lớn chứa các file
folder_path = r"C:\Users\Administrator\Desktop\AIchualanh-main"

# Duyệt qua tất cả các file trong thư mục
for file_name in os.listdir(folder_path):
    if file_name.endswith(".py") and file_name != "run_all.py":  # Chỉ chạy file .py, bỏ qua file 'run_all.py'
        file_path = os.path.join(folder_path, file_name)
        print(f"Running {file_name}...")
        subprocess.run(["python", file_path])
