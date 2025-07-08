
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
from elevenlabs.client import ElevenLabs


API_KEY = "YOUR_ELEVEN_LABS_API_KEY"


VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

client = ElevenLabs(api_key=API_KEY)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

def process_pdf():
    pdf_path = entry.get()
    if not pdf_path.lower().endswith('.pdf'):
        messagebox.showerror("Invalid File", "Please select a valid PDF file.")
        return

    try:
        text = extract_text_from_pdf(pdf_path)
        if not text.strip():
            raise ValueError("No text found in PDF.")
        limited_text = text[:2500]

        audio = client.generate(
            text=limited_text,
            voice=VOICE_ID,
            model="eleven_monolingual_v1"
        )

        with open("output.mp3", "wb") as f:
            f.write(audio)

        messagebox.showinfo("Success", "Audio saved as output.mp3")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

root = tk.Tk()
root.title("PDF to Speech (ElevenLabs)")
root.geometry("400x160")

tk.Label(root, text="Select a PDF file:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Speech", command=process_pdf)
convert_button.pack(pady=10)

root.mainloop()
