from ChatbotController import ChatbotController
from ChatbotModel import ChatbotModel
from ChatbotView import ChatbotView
import tkinter as tk

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    model = ChatbotModel()
    view = ChatbotView(root, None)
    controller = ChatbotController(model, view)
    root.mainloop()
