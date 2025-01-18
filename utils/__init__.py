{
    "version": "1.0",
    "metadata": {
        "created_at": "timestamp",
        "last_updated": "timestamp",
        "total_samples": 1000
    },
    "training_samples": [
        {
            "id": "TR001",
            "timestamp": "2024-01-20T10:30:00Z",
            "user_context": {
                "user_id": "U123",
                "age_group": "18-24",
                "previous_interactions": 5
            },
            "message": {
                "text": "Tôi cảm thấy lo lắng và không thể ngủ được",
                "language": "vi",
                "detected_keywords": ["lo lắng", "mất ngủ"]
            },
            "emotional_analysis": {
                "primary_emotion": "anxiety",
                "secondary_emotions": ["stress", "restlessness"],
                "intensity_level": 7,
                "risk_level": "medium"
            },
            "classification": {
                "label": 1,
                "confidence_score": 0.95,
                "category": "sleep_anxiety"
            },
            "suggested_responses": [
                {
                    "text": "...",
                    "approach": "empathetic_listening",
                    "priority": 1
                }
            ],
            "treatment_path": {
                "immediate_actions": [...],
                "follow_up_suggestions": [...]
            }
        }
    ],
    "validation_metrics": {
        "accuracy": 0.92,
        "f1_score": 0.89,
        "validation_date": "timestamp"
    }
}
