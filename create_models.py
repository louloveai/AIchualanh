import joblib
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def create_models():
    try:
        # Tạo thư mục models nếu chưa có
        os.makedirs('models', exist_ok=True)
        
        # Tạo và save models
        vectorizer = CountVectorizer(max_features=1000)
        joblib.dump(vectorizer, 'models/vectorizer.pkl')
        
        lda_model = LatentDirichletAllocation(n_components=10)
        joblib.dump(lda_model, 'models/lda_model.pkl')
        
        print("✅ Models created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating models: {e}")
        return False

if __name__ == "__main__":
    create_models() 
