import sys
from src.gui.pyqt_gui import Application as PyQtApplication
from src.gui.tk_gui import Application as TkApplication
from PyQt6.QtWidgets import QApplication
import tkinter as tk
import ttkbootstrap as ttkb


def run_pyqt_gui():
    app = QApplication(sys.argv)
    ex = PyQtApplication()
    ex.show()
    sys.exit(app.exec())


def run_tk_gui():
    app = TkApplication()
    app.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tk":
        run_tk_gui()
    else:
        run_pyqt_gui()
