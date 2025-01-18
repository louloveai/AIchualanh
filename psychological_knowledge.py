class PsychologyKnowledge:
    def __init__(self):
        self.knowledge_base = {
            'cognitive_behavioral': {
                'techniques': {
                    'suy_nghi_tich_cuc': {
                        'description': 'Kỹ thuật thay đổi suy nghĩ tiêu cực thành tích cực',
                        'steps': [
                            'Nhận diện suy nghĩ tiêu cực',
                            'Thách thức suy nghĩ đó',
                            'Tìm góc nhìn tích cực hơn'
                        ],
                        'examples': [
                            'Thay vì nghĩ "Mình làm gì cũng sai", hãy nghĩ "Mình đang học hỏi và tiến bộ"'
                        ]
                    },
                    'giai_quyet_van_de': {
                        'description': 'Phương pháp giải quyết vấn đề theo bước',
                        'steps': [
                            'Xác định vấn đề cụ thể',
                            'Liệt kê các giải pháp có thể',
                            'Đánh giá pros/cons',
                            'Chọn và thực hiện giải pháp tốt nhất'
                        ]
                    }
                },
                'exercises': {
                    'thien_mindfulness': {
                        'description': 'Các bài tập thiền mindfulness',
                        'duration': '5-15 phút',
                        'instructions': [
                            'Tìm nơi yên tĩnh',
                            'Tập trung vào hơi thở',
                            'Quan sát suy nghĩ không phán xét'
                        ]
                    }
                }
            },
            'emotional_regulation': {
                'techniques': {
                    'ky_thuat_54321': {
                        'description': 'Kỹ thuật giảm lo âu 5-4-3-2-1',
                        'steps': [
                            '5 thứ bạn nhìn thấy',
                            '4 thứ bạn có thể chạm vào',
                            '3 thứ bạn nghe được',
                            '2 thứ bạn ngửi được',
                            '1 thứ bạn nếm được'
                        ]
                    },
                    'box_breathing': {
                        'description': 'Kỹ thuật thở hộp để kiểm soát cảm xúc',
                        'steps': [
                            'Hít vào đếm 4',
                            'Giữ hơi đếm 4',
                            'Thở ra đếm 4',
                            'Giữ đếm 4'
                        ]
                    }
                }
            },
            'relationship_counseling': {
                'common_issues': {
                    'family_conflict': {
                        'signs': ['Cãi vã thường xuyên', 'Thiếu giao tiếp', 'Kỳ vọng cao'],
                        'solutions': [
                            'Lắng nghe tích cực',
                            'Đặt ranh giới lành mạnh',
                            'Trao đổi về kỳ vọng'
                        ]
                    },
                    'work_stress': {
                        'signs': ['Kiệt sức', 'Lo lắng về deadline', 'Khó tập trung'],
                        'solutions': [
                            'Quản lý thời gian',
                            'Đặt ranh giới công việc-cuộc sống',
                            'Thực hành tự chăm sóc'
                        ]
                    }
                }
            }
        }
        
    def get_technique(self, issue_type, problem):
        """Lấy kỹ thuật phù hợp với vấn đề"""
        if issue_type in self.knowledge_base:
            techniques = self.knowledge_base[issue_type]['techniques']
            # Tìm kỹ thuật phù hợp nhất
            return self._find_best_technique(techniques, problem)
        return None
        
    def get_exercise(self, emotion, intensity):
        """Gợi ý bài tập dựa trên cảm xúc"""
        exercises = []
        if emotion == 'lo_lang' and intensity > 7:
            exercises.append(self.knowledge_base['emotional_regulation']
                          ['techniques']['ky_thuat_54321'])
        elif emotion == 'stress':
            exercises.append(self.knowledge_base['cognitive_behavioral']
                          ['exercises']['thien_mindfulness'])
        return exercises
        
    def get_relationship_advice(self, relationship_type, issue):
        """Tư vấn về các mối quan hệ"""
        if relationship_type in self.knowledge_base['relationship_counseling']['common_issues']:
            return self.knowledge_base['relationship_counseling']['common_issues'][relationship_type]
        return None 