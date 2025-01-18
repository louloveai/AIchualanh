from bs4 import BeautifulSoup

# Đường dẫn đến file HTML của bạn
file_path = "path/to/your/file.html"

# Đọc và xử lý file HTML
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Sử dụng BeautifulSoup để phân tích file HTML
soup = BeautifulSoup(content, "lxml")

# Lấy tất cả nội dung văn bản trong bài viết (bỏ thẻ HTML)
text = soup.get_text(separator="\n")

# Lưu nội dung vào file text để kiểm tra
output_path = "output_text.txt"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(text)

print(f"Nội dung đã được lưu tại: {output_path}")
