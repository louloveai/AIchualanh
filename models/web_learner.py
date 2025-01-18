import requests
from bs4 import BeautifulSoup
from googlesearch import search
import pandas as pd

class WebLearner:
    def __init__(self):
        self.training_data = []
        
    def learn_from_url(self, url):
        try:
            # 1. Đọc bài báo gốc
            content = self.get_article_content(url)
            
            # 2. Tìm từ khóa quan trọng
            keywords = self.extract_keywords(content)
            
            # 3. Tự tìm bài liên quan trên Google
            related_urls = self.find_related_articles(keywords)
            
            # 4. Thu thập nội dung từ các bài liên quan
            for related_url in related_urls:
                related_content = self.get_article_content(related_url)
                if related_content:
                    self.training_data.append({
                        'url': related_url,
                        'content': related_content
                    })
            
            return True
            
        except Exception as e:
            print(f"Error learning from URL: {e}")
            return False
            
    def get_article_content(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article') or soup.find('div', class_='article-content')
        return article.get_text() if article else None
        
    def find_related_articles(self, keywords, num_results=5):
        query = ' '.join(keywords)
        return list(search(query, num_results=num_results))
        
    def extract_keywords(self, content):
        # Implement keyword extraction logic
        # Có thể dùng NLP để trích xuất từ khóa
        pass
        
    def save_training_data(self):
        df = pd.DataFrame(self.training_data)
        df.to_csv('data/raw/web_learned_data.csv', index=False)
