class SafeLearning:
    def __init__(self):
        self.gen_z_topics = {
            'career_anxiety': [
                'định hướng nghề nghiệp',
                'sợ thất bại',
                'áp lực công việc',
                'startup',
                'side hustle'
            ],
            'social_pressure': [
                'social media',
                'comparison trap',
                'influencer',
                'lifestyle',
                'relationship goals'
            ],
            'mental_wellness': [
                'self-care',
                'mental health',
                'work-life balance',
                'burnout',
                'mindfulness'
            ],
            'personal_growth': [
                'self-improvement',
                'skill development',
                'personal branding',
                'financial freedom'
            ]
        }
        
    def analyze_content_relevance(self, text):
        """Phân tích độ phù hợp của nội dung với Gen Z"""
        relevance_score = 0
        for category, keywords in self.gen_z_topics.items():
            if any(keyword in text.lower() for keyword in keywords):
                relevance_score += 1
        return relevance_score > 0 