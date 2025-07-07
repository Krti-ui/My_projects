import tkinter as tk
from tkinter import font as tkFont
import time

def exit_button(root):
    quit_button = tk.Button(
        root,
        text="Quit",
        font=("Poppins", 12, "bold"),
        bg="#ff4d4d",
        fg="white",
        padx=10,
        pady=5,
        command=root.quit
    )
    quit_button.pack(pady=10)

def clear_entry_if_no_activity(last_key_snapshot):
    if last_key_snapshot == last_key_press:
        entry.delete(0, tk.END)
        status_label.config(text="💥 Cleared due to inactivity!")
        print("Text cleared due to 5 seconds of no typing.")

def on_key_press(event):
    global last_key_press
    last_key_press = time.time()
    status_label.config(text="⏳ Keep typing... (5s timer restarted)")
    root.after(5000, lambda: clear_entry_if_no_activity(last_key_press))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Type or Lose!")
    root.configure(bg="#f0f0f0")

    try:
        poppins = tkFont.Font(family="Poppins", size=12)
    except:
        poppins = ("Helvetica", 12)

    label = tk.Label(
        root,
        text="Start typing! Stop for 5 seconds and you'll lose it!",
        font=("Poppins", 14, "bold"),
        width=40,
        height=4,
        bg="#f0f0f0",
        fg="#333333",
        wraplength=300,
        justify="center"
    )
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Poppins", 12), width=30, justify="center")
    entry.pack(pady=10)

    status_label = tk.Label(root, text="", font=("Poppins", 10), fg="red", bg="#f0f0f0")
    status_label.pack()

    exit_button(root)

    last_key_press = time.time()
    entry.bind("<Key>", on_key_press)

    root.mainloop()
