# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Markdown to PowerPoint converter that transforms Markdown files into PowerPoint presentations. The project supports both GUI and API modes, with two GUI implementations (PyQt6 and tkinter) and programmatic access via the converter module.

## Development Environment Setup

```bash
# Create and activate conda environment
conda create -n hackmd_ppt python==3.11.8 -y
conda activate hackmd_ppt

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

### GUI Applications
```bash
# Run PyQt6 GUI (default)
python main.py

# Run tkinter GUI
python main.py --tk

# Platform-specific scripts
# Windows:
Start_GUI.bat

# Linux/macOS:
sh Start_GUI.sh
```

### API Usage
```python
from src.converter.converter import MarkdownToPptConverter

# Mode 0: Markdown content as string
converter = MarkdownToPptConverter(markdown_content, 'output.pptx', mode=0)

# Mode 1: Markdown content as file path
converter = MarkdownToPptConverter('input.md', 'output.pptx', mode=1)

converter.convert()
```

## Building Executables

### Using PyInstaller
```bash
# Install PyInstaller (already in requirements.txt)
pip install pyinstaller

# Build using spec file
pyinstaller Markdown_to_PPT_Converter.spec

# Output will be in dist/ folder
```

### Notes for Building
- Update icon paths in `Markdown_to_PPT_Converter.spec` before building
- The spec file includes the `src` directory in the data files
- Built executables will be created in the `dist/` folder

## Project Architecture

### Core Components

**Main Entry Point** (`main.py:21-25`)
- Handles GUI selection based on command line arguments
- Defaults to PyQt6 GUI, falls back to tkinter with `--tk` flag

**Converter Module** (`src/converter/converter.py:16`)
- `MarkdownToPptConverter` class handles markdown to PowerPoint conversion
- Supports two input modes: string content (mode=0) or file path (mode=1)
- Processes markdown sections separated by `---` as individual slides
- Handles images from both Markdown syntax `![](url)` and HTML `<img>` tags

**GUI Implementations**
- `src/gui/pyqt_gui.py` - PyQt6-based GUI interface
- `src/gui/tk_gui.py` - tkinter/ttkbootstrap-based GUI interface

**Utilities** (`src/utils/file_operations.py`)
- File operations, image downloading, and directory management functions

### Markdown Format Requirements
- Use `---` as slide separators
- First slide with `# Title` becomes the cover slide
- Subsequent slides with `## Heading` become content slides
- Supports bullet points with `- ` prefix
- Handles embedded images via URLs
- Bold text markers `**` are automatically removed during conversion

### Dependencies
- `python-pptx==0.6.19` - PowerPoint manipulation
- `markdown==3.3.4` - Markdown processing
- `PyQt6` - Primary GUI framework
- `ttkbootstrap` - Enhanced tkinter styling
- `requests` - Image downloading
- `PyInstaller==4.5.1` - Executable building