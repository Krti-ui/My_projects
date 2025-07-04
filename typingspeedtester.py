//typing speed tester
import tkinter as tk
from tkinter import messagebox
import time
import random

sample_texts = [
    "The sun is shining brightly today. Birds are singing in the trees. It is a good day for a walk.",
    "The quick brown fox jumps over the lazy dog.",
    "A gentle breeze rustled the leaves as the sun dipped below the horizon, painting the sky in hues of orange and pink.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Artificial intelligence is transforming industries by automating tasks, improving efficiency, and unlocking new possibilities.",
    "He opened the old wooden box with trembling hands, not knowing what memories might be hidden inside.",
    "Water covers about 71% of the Earth's surface, with oceans holding roughly 96.5% of all Earth's water.",
    "Effective communication and teamwork are essential for the success of any organization, regardless of size.",
    "A balanced diet, regular exercise, and sufficient sleep are key components of a healthy lifestyle.",
    "In a world that changes rapidly, adaptability and continuous learning have become essential skills. Those who embrace new challenges and keep an open mind are more likely to thrive in both personal and professional settings."
]


class SpeedTest:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test!")
        self.start_time = None
        self.timer_started = False

        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.main_frame, text="Typing Speed Test", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=(0, 15))

        self.sample_text = random.choice(sample_texts)
        self.text_display = tk.Text(self.main_frame, height=5, wrap='word', font=("Helvetica", 12))
        self.text_display.insert("1.0", self.sample_text)
        self.text_display.config(state='disabled')
        self.text_display.pack(pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Text(self.main_frame, height=5, wrap='word', font=("Helvetica", 12))
        self.entry.pack(pady=10, fill=tk.BOTH, expand=True)
        self.entry.focus_set()
        self.entry.bind("<KeyPress>", self.start_timer)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        self.button = tk.Button(self.button_frame, text="Submit", command=self.check_speed, width=10)
        self.button.pack(side=tk.LEFT, padx=5)
        self.button.config(state="disabled")

        self.restart = tk.Button(self.button_frame, text="Restart", command=self.restart, width=10)
        self.restart.pack(side=tk.LEFT, padx=5)

        self.result_frame = tk.Frame(self.main_frame, bg="#f0f0f0", padx=10, pady=10)
        self.result_frame.pack(pady=10, fill=tk.X)

        self.result_label = tk.Label(self.result_frame, text="Your results will appear here",
                                     font=("Helvetica", 12), bg="#f0f0f0")
        self.result_label.pack()

    def start_timer(self, event):
        if not self.timer_started:
            self.start_time = time.time()
            self.timer_started = True
            self.button.config(state="normal")

    def check_speed(self):
        if not self.timer_started:
            messagebox.showwarning("Warning", "Please start typing first!")
            return

        end_time = time.time()
        final_time = end_time - self.start_time

        typed_text = self.entry.get("1.0", tk.END).strip()
        word_count = len(typed_text.split())

        minutes = final_time / 60
        wpm = word_count / minutes if minutes > 0 else 0

        original_words = self.sample_text.split()
        typed_words = typed_text.split()

        correct_words = 0
        min_length = min(len(original_words), len(typed_words))
        for i in range(min_length):
            if original_words[i] == typed_words[i]:
                correct_words += 1

        accuracy = (correct_words / len(original_words)) * 100 if original_words else 0

        result = f"Time: {final_time:.2f} sec | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result)

        self.timer_started = False
        self.button.config(state="disabled")

    def restart(self):
        self.start_time = None
        self.timer_started = False
        self.entry.delete("1.0", tk.END)
        self.sample_text = random.choice(sample_texts)
        self.text_display.config(state='normal')
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert("1.0", self.sample_text)
        self.text_display.config(state='disabled')
        self.button.config(state="disabled")
        self.result_label.config(text="Your results will appear here")
        self.entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTest(root)
    root.geometry("600x500")
    root.mainloop()
