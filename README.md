# Markdown to PowerPoint Converter

This project converts Markdown files to PowerPoint presentations.
You can use this [GPTs](https://chat.openai.com/g/g-YiXZ7cBcg-markdown-presentation-creator) to generate the base of the Markdown file.

## Installation

Follow these steps to set up a Python virtual environment and install the required packages:

1. Clone this repository:

    ```bash
    git clone https://github.com/treeleaves30760/Hackmd_PPT_Converter
    cd Hackmd_PPT_Converter
    ```

2. Install the required packages:

    ```bash
    conda create -n hackmd_ppt python==3.11.8 -y
    conda activate hackmd_ppt
    pip install -r requirements.txt
    ```

## Usage

### GUI

If you want to use the GUI, you can run the GUI script:

- Windows:

    ```bash
    Start_GUI.bat
    ```

- Linux/macOS:

    ```bash
    sh Start_GUI.sh
    ```

In the GUI, you can input the hackmd code into the textarea, then press the convert button to generate the PPT.

### API

You can import the converter.py:

```python
from src.converter.converter import MarkdownToPptConverter

converter = MarkdownToPptConverter('', 'example.pptx', mode=1)
converter.convert('example.md')
```

## Build Instructions

To create standalone executables for Windows and macOS, follow these steps:

### Prerequisites

1. Ensure you have PyInstaller installed:

   ```bash
   pip install pyinstaller
   ```

2. Make sure your project structure is correctly set up.

### Building the Application

1. Create icon files for your application:
   - For Windows: Create a .ico file
   - For macOS: Create a .icns file

2. Update the `build_release.py` script in the project root with the correct paths to your icon files.

3. To build the application:

   - On Windows:

     ```bash
     python build_release.py
     ```

   - On macOS:

     ```bash
     python build_release.py
     ```

4. The executable will be created in the `dist` folder.

### Distribution

- For Windows: Distribute the .exe file from the `dist` folder.
- For macOS: Distribute the .app file from the `dist` folder.

### Notes

- Test the executables thoroughly on fresh systems to ensure all dependencies are correctly bundled.
- You may need to adjust the PyInstaller arguments in `build_release.py` based on your specific project structure and requirements.
- Consider using tools like Inno Setup (Windows) or Disk Utility (macOS) to create installers or DMG files for easier distribution.

## Format

Below is an example of a markdown file:

```markdown
# Introduction to Stable Diffusion

---

## Table of Contents

1. What is Stable Diffusion?
2. Core Features
3. Use Cases
4. Advantages
5. Limitations

---

## What is Stable Diffusion?

Stable Diffusion is a deep learning model used for generating high-quality images. It can create images based on textual descriptions or edit and enhance existing images.

---

## Core Features

- **Text-to-Image Conversion**: Ability to generate images based on natural language descriptions.
- **Image-to-Image Transformation**: Can transform input images into images of a different style.
- **High-Resolution Support**: Capable of generating high-quality, high-resolution images.
- **Wide Range of Applications**: Suitable for various fields such as art creation, game development, entertainment industry, etc.

---

## Use Cases

- **Art Creation**: Artists and designers use Stable Diffusion to create new artworks.
- **Content Generation**: Automatically generate visual content for social media, advertising, and other domains.
- **Game Development**: Generate game scenes, characters, or textures.

---

## Advantages

- **Fast and Efficient**: Stable Diffusion can generate high-quality images faster compared to traditional image generation techniques.
- **Flexibility**: Users can control the style and details of the generated images by adjusting parameters.

---

## Limitations

- **Creative Constraints**: Generated images may be limited by the training data and may not always fully meet the user's creative requirements.
- **Quality Fluctuations**: While it can produce high-quality images most of the time, there may be instances of unstable image quality.
```

| Usage         | Sign  | Example                         |
|---------------|-------|----------------------------------|
| Page break    | `---` | `---`                            |
| Title         | `#`   | `# PPT to AI`                    |
| Page Title    | `##`  | `## What is AI`                  |
| List Number   | `1.`  | `1. **The usage of AI**`         |
| List Points   | `-`   | `- **AI Development**`           |