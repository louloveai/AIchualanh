from deep_translator import GoogleTranslator
from transformers import pipeline
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def process_data(input_file, output_file):
    # Kiểm tra file input
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File input {input_file} không tồn tại!")
    
    # Đọc dữ liệu
    logging.info("Đọc dữ liệu từ file...")
    data = pd.read_csv(input_file)

    # Lọc dữ liệu
    logging.info("Lọc dữ liệu với từ khóa liên quan...")
    keywords = ["stress", "healing", "anxiety", "mental health", "calm", "relaxation"]
    if "message" not in data.columns:
        raise ValueError("Cột 'message' không tồn tại trong dữ liệu.")
    data = data[data['message'].str.contains('|'.join(keywords), case=False, na=False)]

    # Xử lý dịch ngôn ngữ
    logging.info("Dịch nội dung sang tiếng Việt...")
    try:
        data['message_vi'] = data['message'].apply(
            lambda x: GoogleTranslator(source='auto', target='vi').translate(x)
        )
    except Exception as e:
        logging.error(f"Lỗi khi dịch ngôn ngữ: {e}")
        data['message_vi'] = "Dịch thất bại"

    # Tóm tắt nội dung
    logging.info("Tóm tắt nội dung...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    data['summary'] = data['message_vi'].apply(
        lambda x: summarizer(x, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        if len(x.split()) > 50 else "Nội dung quá ngắn để tóm tắt"
    )
    
    # Lưu kết quả
    logging.info(f"Lưu dữ liệu xử lý xong tại {output_file}")
    data.to_csv(output_file, index=False)


# Ví dụ gọi hàm xử lý
if __name__ == "__main__":
    process_data("input_data.csv", "final_data.csv")
