import markdown
from pptx import Presentation
from pptx.util import Inches, Pt

class MarkdownToPptConverter:
    def __init__(self, md_content, ppt_file):
        self.md_content = md_content
        self.ppt_file = ppt_file

    def convert(self):
        # Initialize presentation
        presentation = Presentation()

        # Split markdown content by '---' (assuming each slide ends with '---')
        slides_md = self.md_content.split('---')

        for slide_md in slides_md:
            slide_md = slide_md.strip()

            if slide_md == '':
                continue

            # Create a new slide
            slide_layout = presentation.slide_layouts[1]
            slide = presentation.slides.add_slide(slide_layout)

            # Get title and content
            lines = slide_md.split('\n')
            title = lines[0].strip('# ').strip()
            content = '\n'.join(lines[1:]).strip()

            # Add title and content to slide
            title_placeholder = slide.shapes.title
            title_placeholder.text = title

            content_placeholder = slide.placeholders[1]
            content_placeholder.text = content

        # Save presentation
        presentation.save(self.ppt_file)
    
if __name__ == "__main__":
    converter = MarkdownToPptConverter('example.md', 'example.pptx')
    converter.convert()
