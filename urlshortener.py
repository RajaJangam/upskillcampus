import tkinter as tk
import pyshorteners

def shorten_url():
    long_url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    result_label.config(text=short_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Set the window dimensions and position
window.geometry("400x200")
window.resizable(False, False)

# Create a frame for the content
content_frame = tk.Frame(window)
content_frame.pack(pady=20)

# Create the GUI components
label = tk.Label(content_frame, text="Enter a URL:")
label.pack()

entry = tk.Entry(content_frame, width=40, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(content_frame, text="Shorten", command=shorten_url, font=("Arial", 12), bg="#4caf50", fg="white", relief=tk.FLAT)
button.pack()

result_label = tk.Label(content_frame, text="", font=("Arial", 12), wraplength=300)
result_label.pack(pady=10)

# Customize the window background color
window.configure(bg="#f0f0f0")

# Start the main GUI loop
window.mainloop()

