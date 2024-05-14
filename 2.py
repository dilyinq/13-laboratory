import tkinter as tk
import requests

class bored:
    def __init__(self, root):
        self.root = root
        self.root.title("bored")
        self.root.geometry("600x500")
        self.root.configure(bg="pink")
# создаем кнопку для нажатия
        self.get_fact_button = tk.Button(self.root, text="Хочу найти себе занятие", font=('arial', 20), command=self.display_fact, bg='white', fg='black')
        self.get_fact_button.pack()
        self.fact_label = tk.Label(self.root, text="", font=('arial', 16), padx=10, pady=50, fg='white', bg="pink")
        self.fact_label.pack()
# запрос на получение занятия
    def get_bored(self):
        response = requests.get("https://www.boredapi.com/api/activity")
        data = response.json()
        return data['activity']
# нажатие кнопки
    def display_fact(self):
        self.bored_data = self.get_bored()
        self.fact_label.config(text=self.bored_data)
# оздаем функцию main, в которой создаем объект класса bored и запускаем главный цикл программы
def main():
    root = tk.Tk()
    app = bored(root)
    root.mainloop()

if __name__ == "__main__":
    main()
