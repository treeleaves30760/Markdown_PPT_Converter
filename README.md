# HackMD to PowerPoint Converter

This project converts HackMD markdown files to PowerPoint presentations.

## Installation

Follow these steps to set up a Python virtual environment and install the required packages:

1. Clone this repository:

    ```
    git clone https://github.com/treeleaves30760/Hackmd_PPT_Converter
    cd Hackmd_PPT_Converter
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

### GUI

If you want use GUI, you can run the GUI script:

- Window
    ```
    Start_GUI.bat
    ```

- Linux/MacOS
    ```
    Staert_GUI.sh
    ```

In the GUI, you can input the hackmd code into textarea, then press the convert button to generate PPT.

### API

You can import the converter.py

```python=
import converter

converter = MarkdownToPptConverter('', 'example.pptx', mode=1)
converter.convert('example.md')
```
