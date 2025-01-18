import sqlite3
import pandas as pd

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect("chat_history.db")

# Truy vấn dữ liệu lịch sử chat
query = "SELECT user_message, bot_response FROM chat"
data = pd.read_sql_query(query, conn)

# Xuất dữ liệu ra file CSV để dễ xử lý
data.to_csv("chat_history.csv", index=False, encoding="utf-8")
print("Dữ liệu đã được lưu vào chat_history.csv")

# Đóng kết nối
conn.close()
