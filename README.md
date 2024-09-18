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

If you want use GUI, you can run the GUI script:

- Window

    ```bash
    Start_GUI.bat
    ```

- Linux/MacOS

    ```bash
    sh Start_GUI.sh
    ```

In the GUI, you can input the hackmd code into textarea, then press the convert button to generate PPT.

### API

You can import the converter.py

```python=
import converter

converter = MarkdownToPptConverter('', 'example.pptx', mode=1)
converter.convert('example.md')
```

## Format

Below is the example of a markdown file

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

|Usage|Sign|Example|
|-|-|-|
|Page break|```---```|```---```|
|Title|```#```|```# PPT to AI```|
|Page Title|```##```|```## What is AI```|
|List Number |```1.```|```1. **The usage of AI**```|
|List Points |```-```|```- **AI Development**```|

```markdown
# Stable Diffusion 簡介

---

## 目錄

1. 什麼是Stable Diffusion?
2. 核心特點
3. 使用案例
4. 優勢
5. 限制

---

## 什麼是Stable Diffusion?

Stable Diffusion是一種深度學習模型，用於生成高質量的圖像。它可以根據文字描述創建圖像，或對現有圖像進行編輯和增強。

---

## 核心特點

- **文本到圖像的轉換**：能夠根據自然語言描述生成圖像。
- **圖像到圖像的轉換**：可以將輸入圖像轉換成另一風格的圖像。
- **高分辨率支持**：能生成高質量、高分辨率的圖像。
- **廣泛的應用**：適用於藝術創作、遊戲開發、娛樂產業等多個領域。

---

## 使用案例

- **藝術創作**：藝術家和設計師使用Stable Diffusion來創造新的藝術作品。
- **內容生成**：自動生成社交媒體、廣告等領域的視覺內容。
- **遊戲開發**：生成遊戲場景、角色或質感。

---

## 優勢

- **快速且高效**：相比於傳統的圖像生成技術，Stable Diffusion能更快地產生高質量圖像。
- **靈活性**：用戶可以通過調整參數來控制生成圖像的風格和細節。

---

## 限制

- **創意限制**：生成的圖像可能受到訓練數據的限制，有時可能無法完全符合用戶的創意需求。
- **質量波動**：雖然大部分時候能生成高質量圖像，但在某些情況下可能會出現質量不穩定的問題。
```

|用法|符號|示例|
|-|-|-|
|分頁|```---```|```---```|
|標題|```#```|```# AI```|
|頁面標題|```##```|```## 什麼是AI```|
|列表編號|```1.```|```1. **AI的使用方式**```|
|列表項目|```-```|```- **AI的發展**```|
