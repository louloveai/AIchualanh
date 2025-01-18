import os
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_models():
    """Test load models"""
    try:
        # Check paths
        model_dir = 'models'
        if not os.path.exists(model_dir):
            logger.error(f"❌ Thư mục {model_dir} không tồn tại!")
            return False
            
        # Test load models
        vectorizer = joblib.load('models/vectorizer.pkl')
        lda_model = joblib.load('models/lda_model.pkl')
        
        logger.info("✅ Models load thành công!")
        return True
    except Exception as e:
        logger.error(f"❌ Lỗi khi test models: {e}")
        return False

if __name__ == "__main__":
    test_models() 
