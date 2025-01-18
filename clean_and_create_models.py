import os
import joblib
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_old_models():
    """Xóa models cũ nếu tồn tại"""
    try:
        if os.path.exists('models/lda_model.pkl'):
            os.remove('models/lda_model.pkl')
        if os.path.exists('models/vectorizer.pkl'):
            os.remove('models/vectorizer.pkl')
        logger.info("✅ Đã xóa models cũ")
    except Exception as e:
        logger.error(f"❌ Lỗi khi xóa models: {e}")

def create_models():
    """Tạo và lưu models mới"""
    try:
        # Tạo thư mục models
        os.makedirs('models', exist_ok=True)
        
        # Tạo models
        vectorizer = CountVectorizer(max_features=1000)
        lda_model = LatentDirichletAllocation(n_components=10)
        
        # Save models
        joblib.dump(vectorizer, 'models/vectorizer.pkl')
        joblib.dump(lda_model, 'models/lda_model.pkl')
        
        # Verify models
        test_vectorizer = joblib.load('models/vectorizer.pkl')
        test_lda = joblib.load('models/lda_model.pkl')
        
        logger.info("✅ Models đã được tạo và test thành công!")
        return True
    except Exception as e:
        logger.error(f"❌ Lỗi khi tạo models: {e}")
        return False

if __name__ == "__main__":
    clean_old_models()
    create_models()
