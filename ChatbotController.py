

# Controller: ควบคุมการทำงานของ Model และ View
class ChatbotController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self
    
    # ข้อมูลคำตอบจาก model
    def get_response(self, question_type):
        question_type, answer, emotion = self.model.model_send_all_answerw(question_type)
        return question_type, answer, emotion
    
    # ข้อมูลเฉลี่ยจาก logs
    def get_emotion_statistics(self):
        return self.model.get_emotion_statistics()