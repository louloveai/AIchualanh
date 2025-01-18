from deep_translator import GoogleTranslator

def translate_text(text, source_lang="vi", target_lang="en"):
    return GoogleTranslator(source=source_lang, target=target_lang).translate(text)

# Ví dụ chạy
if __name__ == "__main__":
    result = translate_text("Xin chào", source_lang="vi", target_lang="en")
    print(result)
