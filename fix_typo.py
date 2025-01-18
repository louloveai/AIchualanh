import os
import re

def fix_typo_in_files(directory, typo, correction, file_extensions=[".py"], max_file_size_mb=5):
    """
    Quét toàn bộ thư mục và sửa lỗi chính tả trong file mã nguồn.

    Args:
        directory (str): Đường dẫn thư mục.
        typo (str): Lỗi chính tả cần sửa.
        correction (str): Sửa đúng.
        file_extensions (list): Danh sách các loại file cần kiểm tra.
        max_file_size_mb (int): Giới hạn kích thước file tối đa (MB).
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                
                # Kiểm tra kích thước file
                if os.path.getsize(file_path) > max_file_size_mb * 1024 * 1024:
                    print(f"Bỏ qua file lớn: {file_path}")
                    continue
                
                # Đọc nội dung file với mã hóa UTF-8, xử lý lỗi mã hóa
                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                except Exception as e:
                    print(f"Lỗi khi đọc file: {file_path}, {e}")
                    continue

                # Sửa lỗi chính tả
                fixed_content = re.sub(rf"\b{typo}\b", correction, content)

                # Ghi đè file nếu có thay đổi
                if content != fixed_content:
                    try:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(fixed_content)
                        print(f"Đã sửa lỗi trong file: {file_path}")
                    except Exception as e:
                        print(f"Lỗi khi ghi file: {file_path}, {e}")

# Cấu hình đường dẫn thư mục và lỗi cần sửa
if __name__ == "__main__":
    project_directory = "./"  # Thư mục gốc chứa code
    fix_typo_in_files(project_directory, "mport joblib", "import joblib")
