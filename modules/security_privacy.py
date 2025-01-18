class SecurityPrivacy:
    def __init__(self):
        self.security_measures = {
            "mã_hóa": {
                "dữ_liệu": ["end-to-end", "AES-256", "RSA"],
                "truyền_tải": ["SSL/TLS", "HTTPS", "VPN"],
                "lưu_trữ": ["encrypted storage", "secure backup"]
            },
            "quyền_riêng_tư": {
                "ẩn_danh": ["mã hóa ID", "che tên", "bảo vệ thông tin"],
                "kiểm_soát": ["quyền truy cập", "xóa dữ liệu", "xuất dữ liệu"],
                "chính_sách": ["GDPR", "HIPAA", "CCPA"]
            }
        } 