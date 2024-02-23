import tkinter as tk
from tkinter.ttk import Progressbar
import converter


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("320x640")
        self.create_widgets()

    def create_widgets(self):
        self.textarea = tk.Text(self, height=10)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        self.button = tk.Button(self, text="Convert", command=self.convert)
        self.button.pack(fill=tk.BOTH)

        self.progress = Progressbar(self, length=200, mode="determinate")
        self.progress.pack(fill=tk.BOTH)

    def convert(self):
        # Get the text from the textarea
        md_content = self.textarea.get("1.0", "end")

        # Convert the markdown content to pptx
        Converter = converter.MarkdownToPptConverter(md_content, "output.pptx")
        Converter.convert()

        # Update the progress bar
        self.progress["value"] = 100


app = Application()
app.mainloop()
