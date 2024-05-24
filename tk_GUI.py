import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import ttkbootstrap as ttkb  # Import ttkbootstrap
from ttkbootstrap.constants import *  # Import constants for easy access to styles
import webbrowser
import os
import converter


class Application(ttkb.Window):
    def __init__(self, *args, **kwargs):
        """
        Initialize the application with ttkbootstrap.
        Set the window size and title, and create the widgets using ttkbootstrap styles.
        """
        super().__init__(*args, **kwargs)
        self.geometry("640x640")
        self.title("Markdown to PPT Converter By Hsu Po Hsiang")
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the application using ttkbootstrap.
        """
        # Create a frame to contain the widgets
        frame = ttkb.Frame(self, bootstyle=SECONDARY)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a label for the textarea with ttkbootstrap styling
        self.textarea = tk.Text(frame, height=10)
        self.textarea.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create buttons with ttkbootstrap styles
        import_button = ttkb.Button(
            frame,
            text="Import Markdown File",
            command=self.import_file,
            bootstyle=(PRIMARY, OUTLINE),
        )
        import_button.pack(fill=tk.BOTH, padx=5, pady=5)

        self.button = ttkb.Button(
            frame, text="Convert", command=self.convert, bootstyle=SUCCESS
        )
        self.button.pack(fill=tk.BOTH, padx=5, pady=5)

        # Create a progress bar with ttkbootstrap style
        self.progress = ttkb.Progressbar(frame, length=200, bootstyle=(INFO, STRIPED))
        self.progress.pack(fill=tk.BOTH, padx=5, pady=5)

        # Create an open folder button with ttkbootstrap style
        open_folder_button = ttkb.Button(
            frame,
            text="Open Output Folder",
            command=self.open_output_folder,
            bootstyle=(DANGER, OUTLINE),
        )
        open_folder_button.pack(fill=tk.BOTH, padx=5, pady=5)

    def import_file(self):
        """
        Open a file dialog to import a markdown file.
        """
        file_path = filedialog.askopenfilename(
            title="Open file",
            filetypes=[("Markdown files", "*.md"), ("Text files", "*.txt")],
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.textarea.delete(1.0, tk.END)  # Clear the textarea
                self.textarea.insert(tk.END, file.read())  # Insert file content

    def convert(self):
        """
        Convert the markdown content to a PowerPoint presentation.
        """
        md_content = self.textarea.get("1.0", tk.END)
        output_filename = simpledialog.askstring(
            "Output File Name",
            "Enter the name of the output PPTX file:",
            initialvalue="output.pptx",
        )
        if "pptx" not in output_filename:
            output_filename += ".pptx"
        if output_filename:
            Converter = converter.MarkdownToPptConverter(md_content, output_filename)
            self.progress["value"] = 50
            Converter.convert()
            self.progress["value"] = 100
            messagebox.showinfo(
                "Conversion Completed",
                f"File has been converted and saved as {output_filename}",
            )

    def open_output_folder(self):
        """
        Open the output folder in the file manager.
        """
        output_folder_path = os.path.abspath(os.path.dirname(__file__))

        # For macOS, we use "open", and for Linux, we use "xdg-open".
        try:
            webbrowser.open("file://" + output_folder_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open the output folder: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
