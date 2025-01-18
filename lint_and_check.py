import subprocess
import os

def check_requirements():
    print("Đang kiểm tra dependencies trong requirements.txt...")
    try:
        result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Tất cả dependencies đã được cài đặt thành công!")
        else:
            print("Lỗi dependencies:\n", result.stderr)
    except Exception as e:
        print("Lỗi khi kiểm tra requirements:", str(e))

def check_python_files(directory="."):
    print("\nĐang kiểm tra lỗi trong các file Python...")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    subprocess.run(["python", "-m", "py_compile", file_path], check=True)
                    print(f"✅ File {file} không có lỗi.")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Lỗi trong file {file}:\n", e.stderr)

if __name__ == "__main__":
    print("=== Bắt đầu kiểm tra dự án ===")
    try:
        check_requirements()
        check_python_files()
        print("✅ Kiểm tra hoàn tất: Không có lỗi nào!")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi trong quá trình kiểm tra: {e}")
