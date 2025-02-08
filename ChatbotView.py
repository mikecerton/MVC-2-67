
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ChatbotController

# View: จัดการ UI
class ChatbotView:
    def __init__(self, root, controller):
        self.controller = controller
        root.title("AI Chatbot")
        root.geometry("400x300")
        
        tk.Label(root, text="เลือกประเภทคำถาม").pack()
        self.question_type_var = tk.StringVar()
        self.question_type_dropdown = ttk.Combobox(root, textvariable=self.question_type_var, values=["วิทยาศาสตร์", "ความรู้ทั่วไป", "คําถามเชิงอารมณ์"])
        self.question_type_dropdown.pack()
        
        self.submit_button = tk.Button(root, text="ถาม AI", command=self.ask_question)
        self.submit_button.pack(pady=5)

        self.ques_type = tk.Label(root, text="")
        self.ques_type.pack()
        
        self.answer_label = tk.Label(root, text="")
        self.answer_label.pack()
        
        self.emotion_label = tk.Label(root, text="")
        self.emotion_label.pack()

        self.avg_all3_label = tk.Label(root, text="")
        self.avg_all3_label.pack()

        self.avg_sci_label = tk.Label(root, text="")
        self.avg_sci_label.pack()

        self.avg_general_label = tk.Label(root, text="")
        self.avg_general_label.pack()
        
        self.avg_emotion_label = tk.Label(root, text="")
        self.avg_emotion_label.pack()


    def ask_question(self):
        question_type = self.question_type_var.get()
        if question_type:
            question_type, answer, emotion = self.controller.get_response(question_type)
            self.ques_type.config(text=f"ประเภทของคําถาม : {question_type}")
            self.answer_label.config(text=f"คำตอบของ Chatbot : {answer}")
            self.emotion_label.config(text=f"ระดับอารมณ์ : {emotion}%")

            overall_avg, avg_sci, avg_general, avg_emotion = self.controller.get_emotion_statistics()
            self.avg_all3_label.config(text=f"ค่าเฉลี่ยของอารมณ์รวม 3 แบบ : {overall_avg}%")
            self.avg_sci_label.config(text=f"ค่าเฉลี่ยของอารมณ์ วิทยาศาสตร์ : {avg_sci}%")
            self.avg_general_label.config(text=f"ค่าเฉลี่ยของอารมณ์ ความรู้ทั่วไป : {avg_general}%")
            self.avg_emotion_label.config(text=f"ค่าเฉลี่ยของอารมณ์ คําถามเชิงอารมณ์: {avg_emotion}%")

