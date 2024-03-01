import markdown
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        self.data = data


class MarkdownToPptConverter:
    def __init__(self, md_content, ppt_file, mode=0):
        self.md_content = md_content
        self.ppt_file = ppt_file
        self.mode = mode

    def convert(self):
        # Initialize presentation
        presentation = Presentation()
        first_slide_created = False
        if self.mode == 1:
            with open(self.md_content_file, "r") as f:
                self.md_content = f.read()

            self.md_content = markdown.markdown(self.md_content)

        # Split markdown content by '---'
        slides_md = self.md_content.split("---")
        for slide_md in slides_md:
            slide_md = slide_md.strip()

            if slide_md == "":
                continue

            # Split title and content
            lines = slide_md.split("\n")
            title_line = lines[0].strip()
            content_lines = lines[1:]

            # Check if it's the first slide (cover page)
            if title_line.startswith("# ") and not first_slide_created:
                # Create cover slide
                slide_layout = presentation.slide_layouts[5]  # Title Slide
                slide = presentation.slides.add_slide(slide_layout)
                title = title_line.strip("# ").strip().replace("**", "")
                slide.shapes.title.text = title
                first_slide_created = True
            else:
                # Create a new slide for content
                slide_layout = presentation.slide_layouts[1]  # Title and Content
                slide = presentation.slides.add_slide(slide_layout)

                title = title_line.strip("# ").strip().replace("**", "")
                slide.shapes.title.text = title

                # Process content
                tf = slide.placeholders[1].text_frame
                tf.text = ""  # Clear default text

                for line in content_lines:
                    line = line.replace("**", "")  # Remove '**' from line
                    if line.startswith("- "):  # Check for bullet points
                        p = tf.add_paragraph()
                        p.text = line.strip("- ")
                        p.level = 0  # Adjust level as needed for nested bullets
                    elif line.strip():  # Non-empty line that doesn't start with '-'
                        p = tf.add_paragraph()
                        p.text = line
                        p.level = 0

        # Save presentation
        presentation.save(self.ppt_file)


# Example usage
if __name__ == "__main__":
    md_content = """ 
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
"""
    converter = MarkdownToPptConverter(md_content, "example.pptx", mode=0)
    converter.convert()
