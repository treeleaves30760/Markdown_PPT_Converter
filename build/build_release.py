import PyInstaller.__main__
import sys
import os


def build_release():
    # Determine the correct main file and icon based on the platform
    if sys.platform == "darwin":  # macOS
        main_file = "main.py"
        icon_file = "path/to/your/mac_icon.icns"
    elif sys.platform == "win32":  # Windows
        main_file = "main.py"
        icon_file = "path/to/your/windows_icon.ico"
    else:
        print(f"Unsupported platform: {sys.platform}")
        return

    # PyInstaller command line arguments
    args = [
        main_file,
        '--onefile',
        '--windowed',
        f'--icon={icon_file}',
        '--add-data=src:src',  # Include the src directory
        '--name=Markdown_to_PPT_Converter',
    ]

    # Run PyInstaller
    PyInstaller.__main__.run(args)


if __name__ == "__main__":
    build_release()
