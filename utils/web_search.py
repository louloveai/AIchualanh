import logging
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
import json
import hashlib
import redis
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from nltk.tokenize import sent_tokenize
from transformers import pipeline

class AdvancedWebSearchHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # Redis cache
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        # Sentiment analyzer
        self.sentiment_analyzer = pipeline('sentiment-analysis')
        # Content summarizer
        self.summarizer = pipeline('summarization')
        
    def _generate_cache_key(self, query: str) -> str:
        """Generate unique cache key for query"""
        return f"websearch:{hashlib.md5(query.encode()).hexdigest()}"

    def _get_cached_result(self, query: str) -> Optional[Dict]:
        """Get cached search result if exists"""
        cache_key = self._generate_cache_key(query)
        cached = self.redis_client.get(cache_key)
        if cached:
            result = json.loads(cached)
            # Check if cache is still valid (24 hours)
            if datetime.fromisoformat(result['cached_at']) > datetime.now() - timedelta(hours=24):
                self.logger.info(f"Cache hit for query: {query}")
                return result
        return None

    def _cache_result(self, query: str, result: Dict):
        """Cache search result with timestamp"""
        cache_key = self._generate_cache_key(query)
        result['cached_at'] = datetime.now().isoformat()
        self.redis_client.setex(
            cache_key,
            timedelta(hours=24),
            json.dumps(result)
        )

    async def _fetch_url_content(self, url: str) -> Optional[Dict]:
        """Fetch and process content from URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer']):
                element.decompose()
                
            content = soup.get_text(separator=' ', strip=True)
            
            # Basic content cleaning
            content = ' '.join(content.split())
            
            # Sentiment analysis
            sentiment = self.sentiment_analyzer(content[:512])[0]
            
            # Summarize long content
            if len(content) > 1000:
                summary = self.summarizer(content[:1000])[0]['summary_text']
            else:
                summary = content
                
            return {
                'url': url,
                'content': content,
                'summary': summary,
                'sentiment': sentiment,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None

    async def search_and_get_answer(self, 
                                  query: str, 
                                  num_results: int = 5,
                                  max_workers: int = 3) -> Dict:
        """Search web and get processed answer"""
        try:
            # Check cache first
            cached_result = self._get_cached_result(query)
            if cached_result:
                return cached_result

            # Perform Google search
            search_results = search(query, lang='vi', num_results=num_results)
            
            # Fetch content from URLs in parallel
            contents = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [
                    executor.submit(self._fetch_url_content, url)
                    for url in search_results
                ]
                for future in futures:
                    if result := future.result():
                        contents.append(result)

            if not contents:
                raise Exception("No valid content found")

            # Process and combine results
            combined_result = {
                'source': 'web_search',
                'query': query,
                'results': contents,
                'summary': self._generate_combined_summary(contents),
                'sentiment_analysis': self._analyze_overall_sentiment(contents),
                'urls': [c['url'] for c in contents],
                'timestamp': datetime.now().isoformat()
            }

            # Cache the result
            self._cache_result(query, combined_result)

            return combined_result

        except Exception as e:
            self.logger.error(f"Search failed: {e}")
            return {
                'source': 'web_search',
                'error': f"Không tìm thấy thông tin phù hợp: {str(e)}",
                'urls': [],
                'timestamp': datetime.now().isoformat()
            }

    def _generate_combined_summary(self, contents: List[Dict]) -> str:
        """Generate a combined summary from all contents"""
        all_summaries = [c['summary'] for c in contents]
        combined_text = ' '.join(all_summaries)
        return self.summarizer(combined_text[:1000])[0]['summary_text']

    def _analyze_overall_sentiment(self, contents: List[Dict]) -> Dict:
        """Analyze overall sentiment from all contents"""
        sentiments = [c['sentiment'] for c in contents]
        return {
            'overall': max(set(sentiments), key=sentiments.count),
            'distribution': {
                label: sentiments.count(label)/len(sentiments)
                for label in set(sentiments)
            }
        }

    def format_response(self, search_result: Dict) -> str:
        """Format search result into user-friendly response"""
        if "error" in search_result:
            return f"""
            Xin lỗi, tôi không tìm thấy thông tin phù hợp.
            Lỗi: {search_result['error']}
            Bạn có thể diễn đạt lại câu hỏi không?
            """

        response = f"""
        Dựa trên thông tin tìm được:
        
        Tóm tắt: {search_result['summary']}
        
        Phân tích cảm xúc: {search_result['sentiment_analysis']['overall']}
        
        Nguồn tham khảo:
        {chr(10).join(f'- {url}' for url in search_result['urls'][:3])}
        
        Thời gian tìm kiếm: {search_result['timestamp']}
        """

        return response.strip() 