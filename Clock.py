import tkinter as tk
from tkinter import ttk
from time import strftime
import time

class Clock(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('460x120')
        self.title('PixClock')
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label_text = "I don't even know why I create these things."
        lbl = tk.Label(self, text=label_text)
        lbl.place(x=60, y=0)

        label_text1 = "Look, I just create these for fun."
        lbl = tk.Label(self, text=label_text1)
        lbl.place(x=120, y=20)

        label_text2 = "As a beginner, I know I am a bit strange with these, xD"
        lbl = tk.Label(self, text=label_text2)
        lbl.place(x=10, y=40)

        button1 = tk.Button(self, text="Timer", command=self.open_timer)
        button1.place(x=180, y=80)

    def open_timer(self):
        timer_window = Timer(self)

    def time(self):
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, self.time)

class Timer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('440x200')
        self.title('Timer')
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        label_text = "Enter time in minutes:"
        lbl = tk.Label(self, text=label_text)
        lbl.pack()

        label_text1 = "Don't forget that 0.1 = 10% of a minute = 6s"
        lbl = tk.Label(self, text=label_text1)
        lbl.pack()

        label_text2 = "Place the number as a floathing point"
        lbl = tk.Label(self, text=label_text2)
        lbl.pack()

        self.timer = tk.Entry(self)
        self.timer.pack()

        start_btn = tk.Button(self, text="Start Timer", command=self.start_timer)
        start_btn.pack()

        self.timer_label = tk.Label(self, text="")
        self.timer_label.pack()

    def start_timer(self):
        try:
            timer_value = float(self.timer.get())
            timer_duration = int(timer_value * 60)
            self.update_timer(timer_duration)
        except ValueError:
            self.timer_label.config(text="Invalid input. Enter a valid number of minutes.")

    def update_timer(self, remaining_time):
        if remaining_time > 0:
            minutes, seconds = divmod(remaining_time, 60)
            self.timer_label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
            self.after(1000, self.update_timer, remaining_time - 1)
        else:
            self.timer_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(root)
    lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='white', foreground='black')
    lbl.pack(anchor='center')
    app.time()
    root.wm_title("PixClock")
    root.geometry("400x100")
    root.mainloop()
