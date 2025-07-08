from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import filedialog
from collections import Counter

def open_img():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    if file_path:
        try:
            image = Image.open(file_path).convert("RGB")
            tk_img = ImageTk.PhotoImage(image)
            image_label.config(image=tk_img)
            image_label.image = tk_img
            status_label.config(text=f"Image loaded: {file_path}")

            image_np = np.array(image)

            pixels = image_np.reshape(-1, 3)

            color_collection = Counter(map(tuple, pixels))
            most_common_colors = color_collection.most_common(5)
            print("Top 5 colors:")
            for color, count in most_common_colors:
                print(f"Color: {color}, Count: {count}")

            top_color = most_common_colors[0][0]
            status_label.config(text=f"Top color: RGB{top_color}")

        except Exception as e:
            status_label.config(text=f"Error loading image: {e}")

root = tk.Tk()
root.title("Image Scanner")
root.geometry("400x300")

open_button = tk.Button(root, text="post image", command=open_img)
open_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

status_label = tk.Label(root, text="No image loaded.")
status_label.pack(pady=5)

root.mainloop()
