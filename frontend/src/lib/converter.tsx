import PptxGenJS from 'pptxgenjs';

interface ImageMatch {
  alt: string;
  url: string;
}

class MarkdownToPptConverter {
  private mdContent: string;
  private presentation: PptxGenJS;

  constructor(mdContent: string) {
    this.mdContent = mdContent;
    this.presentation = new PptxGenJS();
  }

  private parseImageSyntax(line: string): ImageMatch[] {
    const matches: ImageMatch[] = [];
    
    const mdImageRegex = /!\[(.*?)\]\((.*?)\)/g;
    let match;
    while ((match = mdImageRegex.exec(line)) !== null) {
      matches.push({
        alt: match[1],
        url: match[2]
      });
    }

    const htmlImageRegex = /<img.*?src="(.*?)".*?alt="(.*?)".*?>/g;
    while ((match = htmlImageRegex.exec(line)) !== null) {
      matches.push({
        alt: match[2],
        url: match[1]
      });
    }

    return matches;
  }

  private formatContent(contentLines: string[]): { text: string, options: any }[] {
    const formattedLines: { text: string, options: any }[] = [];
    
    contentLines.forEach(line => {
      const trimmedLine = line.trim();
      if (!trimmedLine) return;

      // Handle bold text
      const textWithoutBold = trimmedLine.replace(/\*\*/g, '');

      // Handle bullet points
      if (trimmedLine.startsWith('- ')) {
        formattedLines.push({
          text: textWithoutBold.substring(2),
          options: {
            bullet: { indent: 20 }
          }
        });
      }
      // Handle numbered lists
      else if (/^\d+\.\s/.test(trimmedLine)) {
        formattedLines.push({
          text: textWithoutBold,
          options: {
            bullet: false,
            breakLine: true
          }
        });
      }
      // Regular text
      else {
        formattedLines.push({
          text: textWithoutBold,
          options: {
            bullet: false,
            breakLine: true
          }
        });
      }
    });

    return formattedLines;
  }

  private async processSlideContent(slide: PptxGenJS.Slide, contentLines: string[]): Promise<void> {
    const leftMargin = 0.5;
    const titleHeight = 1.5; // Height reserved for title
    
    // Filter out empty lines
    const nonEmptyLines = contentLines.filter(line => line.trim());
    
    if (nonEmptyLines.length > 0) {
      const formattedContent = this.formatContent(nonEmptyLines);
      
      // Add content as a single text block with multiple paragraphs
      slide.addText(formattedContent.map(item => ({
        text: item.text,
        options: {
          ...item.options,
          breakLine: true // Force line break after each item
        }
      })), {
        x: leftMargin,
        y: titleHeight,
        w: '90%',
        h: 4.5,
        fontSize: 18,
        align: 'left',
        valign: 'top',
        breakLine: true
      });
    }
  }

  public async convert(): Promise<Blob> {
    let firstSlideCreated = false;
    const slides = this.mdContent.split('---');

    for (const slideContent of slides) {
      const trimmedContent = slideContent.trim();
      if (!trimmedContent) continue;

      const lines = trimmedContent.split('\n');
      const titleLine = lines[0].trim();
      const contentLines = lines.slice(1);

      // Handle first slide (cover page)
      if (titleLine.startsWith('# ') && !firstSlideCreated) {
        const slide = this.presentation.addSlide();
        const title = titleLine.replace(/^#\s+/, '').replace(/\*\*/g, '');
        
        slide.addText(title, {
          x: 0.5,
          y: 2,
          w: '90%',
          h: 2,
          fontSize: 44,
          bold: true,
          align: 'center',
          valign: 'middle'
        });
        
        firstSlideCreated = true;
      } else {
        // Create content slide
        const slide = this.presentation.addSlide();
        
        // Add title (removing any number of # characters)
        const title = titleLine.replace(/^#+\s+/, '').replace(/\*\*/g, '');
        slide.addText(title, {
          x: 0.5,
          y: 0.3,
          w: '90%',
          h: 1,
          fontSize: 32,
          bold: true,
          align: 'left',
          valign: 'middle',
          color: '363636'
        });

        // Process slide content
        await this.processSlideContent(slide, contentLines);
      }
    }

    return await this.presentation.writeFile() as unknown as Blob;
  }
}

export default MarkdownToPptConverter;