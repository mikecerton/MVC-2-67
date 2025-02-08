import pandas as pd
import random


# Model: จัดการฐานข้อมูลและตรรกะ
class ChatbotModel:
    def __init__(self, data_file="chatbot_data.csv", log_file="chatbot_logs.csv"):
        self.data_file = data_file
        self.log_file = log_file
        self.previous_question_type = None
        self.previous_emotion = None
        self.emotion_log = []
        self.load_data()
        self.load_logs()

    def load_data(self):
        self.data = pd.read_csv(self.data_file)
        print(len(self.data))

    def load_logs(self):
        self.logs = pd.read_csv(self.log_file)
        print(len(self.logs))

    def save_logs(self):
        self.logs.to_csv(self.log_file, index=False)

    def model_send_all_answerw(self, question_type):
        answer = self.get_random_answer(question_type)

        if question_type == "วิทยาศาสตร์":
            emotion = self.cal_emotion_sci()
            
        elif question_type == "ความรู้ทั่วไป":
            emotion = self.cal_emotion_general()
            
        elif question_type == "คําถามเชิงอารมณ์":
            emotion = self.cal_emotion_emo()
        else:
            emotion = 50
        
        self.previous_question_type = question_type
        self.previous_emotion = emotion
        self.emotion_log.append(question_type)
        new_logg = pd.DataFrame({"question_type": [question_type], "emotion": [emotion], "answer": [answer]})
        self.logs = pd.concat([self.logs, new_logg], ignore_index=True)
        self.save_logs()

        return question_type, answer, emotion
    
    def cal_emotion_sci(self):
        if self.previous_question_type == "อารมณ์" and self.previous_emotion < 30:
            emotion = random.randint(10, 40)
        else:
            emotion = random.randint(50, 80)
        return emotion
    
    def cal_emotion_general(self):
        if self.previous_question_type == "วิทยาศาสตร์" and self.previous_emotion < 60:
                emotion = random.randint(30, 60)
        else:
            emotion = random.randint(70, 100)
        return emotion
    
    def cal_emotion_emo(self):
        if len(self.emotion_log) >= 3 and self.emotion_log[-3:] == ["อารมณ์"] * 3:
                emotion = random.randint(20, 50)
        elif self.previous_emotion is not None:
            emotion = max(0, min(100, self.previous_emotion + random.randint(-10, 10)))
        else:
            emotion = 100
        return emotion
        
    def get_random_answer(self, question_type):
        filtered = self.data[self.data["question_type"] == question_type]
        if not filtered.empty:
            return filtered.sample(n=1)["answer"].values[0]
        return "ไม่มีคำตอบในฐานข้อมูล"

    def get_emotion_statistics(self):
            if self.logs.empty:
                return 0, 0, 0, 0
            
            overall_avg = self.logs["emotion"].mean()
            stats = self.logs.groupby("question_type")["emotion"].mean()
            # print(stats)
            avg_sci = stats["วิทยาศาสตร์"]
            avg_general = stats["ความรู้ทั่วไป"]
            avg_emotion = stats["คําถามเชิงอารมณ์"]

            return overall_avg, avg_sci, avg_general, avg_emotion