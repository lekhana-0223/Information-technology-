import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
       self.quiz_data = [
            {
                "question": "Who wrote the novel 1984?",
                "options": ["George Orwell", "J.K. Rowling", "F. Scott Fitzgerald", "Ernest Hemingway"],
                "correct_answer": 0
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "correct_answer": 2
            },
            {
                "question": "In what year was the first iPhone released?",
                "options": ["2005", "2007", "2008", "2010"],
                "correct_answer": 1
            }
        ]
       self.current_question_index = 0
       self.score = 0
       self.window = tk.Tk()
       self.window.title("Quiz App")
       self.question_label = tk.Label(self.window, text="")
       self.question_label.pack()
       self.options_frame = tk.Frame(self.window)
       self.options_frame.pack()
       self.option_buttons = []
       for i in range(4):
           button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
           button.pack(pady=5)
           self.option_buttons.append(button)

    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer = question_data["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct")
        else:
            messagebox.showinfo("Incorrect", "Your answer is wrong")
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz_data):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score is {self.score} out of {len(self.quiz_data)}")
            self.window.destroy()

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

quiz_app = QuizApp()
quiz_app.start_quiz()

