import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
from tkinter.ttk import Progressbar
import webbrowser
import os
import converter


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("640x640")
        self.title("Markdown to PPT Converter By Hsu Po Hsiang")
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self, bd=10, relief=tk.GROOVE)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.textarea = tk.Text(frame, height=10)
        self.textarea.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        import_button = tk.Button(
            frame, text="Import Markdown File", command=self.import_file
        )
        import_button.pack(fill=tk.BOTH, padx=5, pady=5)

        self.button = tk.Button(frame, text="Convert", command=self.convert)
        self.button.pack(fill=tk.BOTH, padx=5, pady=5)

        self.progress = Progressbar(frame, length=200, mode="determinate")
        self.progress.pack(fill=tk.BOTH, padx=5, pady=5)

        open_folder_button = tk.Button(
            frame, text="Open Output Folder", command=self.open_output_folder
        )
        open_folder_button.pack(fill=tk.BOTH, padx=5, pady=5)

    def import_file(self):
        file_path = filedialog.askopenfilename(
            title="Open file",
            filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt")],
        )  # Allow .md and .txt files
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.textarea.delete(1.0, tk.END)  # Clear the textarea
                self.textarea.insert(tk.END, file.read())  # Insert file content

    def convert(self):
        md_content = self.textarea.get("1.0", tk.END)
        output_filename = simpledialog.askstring(
            "Output File Name",
            "Enter the name of the output PPTX file:",
            initialvalue="output.pptx",
        )
        if output_filename:
            Converter = converter.MarkdownToPptConverter(md_content, output_filename)
            self.progress["value"] = 50
            Converter.convert()
            self.progress["value"] = 100
            tk.messagebox.showinfo(
                "Conversion Completed",
                f"File has been converted and saved as {output_filename}",
            )

    def open_output_folder(self):
        output_folder_path = os.path.abspath(os.path.dirname(__file__))
        # For macOS, we use "open", and for Linux, we use "xdg-open".
        try:
            # Attempt to open the folder in the OS's file manager
            webbrowser.open("file://" + output_folder_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open the output folder: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
