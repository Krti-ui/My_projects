//WaterMarking desktop app
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageDraw, ImageFont


class WaterMarkApp():
    def __init__(self, root):
        self.root = root
        root.title("Image Watermarking App")
        root.geometry("400x180")

        self.image = None
        self.watermarked_image = None
        tk.Button(root, text="Upload Image", command=self.upload_image).pack(pady=8)
        self.watermark_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark, state=tk.DISABLED)
        self.watermark_btn.pack(pady=8)
        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=8)

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if path:
            try:
                self.image = Image.open(path).convert("RGBA")
                self.watermarked_image = None
                self.watermark_btn.config(state=tk.NORMAL)
                self.save_btn.config(state=tk.DISABLED)
                messagebox.showinfo("Loaded", f"Loaded image:\n{path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")

    def add_watermark(self):
        if not self.image:
            return
        text = simpledialog.askstring("Watermark Text", "Enter watermark text:")
        if text:
            try:
                base = self.image.copy()
                width, height = base.size
                layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(layer)

                try:
                    font_size = max(12, height // 20)
                    font = ImageFont.truetype("arial.ttf", font_size)
                except IOError:
                    font = ImageFont.load_default()
                    font_size = 12

                text_bbox = draw.textbbox((0, 0), text, font=font)
                tw, th = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
                pos = (width - tw - 10, height - th - 10)

                draw.text(pos, text, font=font, fill=(255, 255, 255, 128))

                self.watermarked_image = Image.alpha_composite(base, layer).convert("RGB")
                messagebox.showinfo("Success", "Watermark added!")
                self.save_btn.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add watermark:\n{str(e)}")

    def save_image(self):
        if not self.watermarked_image:
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("JPEG files", "*.jpg"),
                ("PNG files", "*.png"),
                ("All files", "*.*")
            ])
        if path:
            try:
                if path.lower().endswith('.jpg') or path.lower().endswith('.jpeg'):
                    self.watermarked_image.save(path, quality=95)
                else:
                    self.watermarked_image.save(path)
                messagebox.showinfo("Saved", f"Image saved at:\n{path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterMarkApp(root)
    root.mainloop()

