from flask import Flask, request, send_file, jsonify, render_template
from src.converter.converter import MarkdownToPptConverter
import os
import tempfile

app = Flask(__name__)

# Configure temp directory for file operations
TEMP_DIR = tempfile.gettempdir()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    """Serve the React app - this will be handled by Vercel's build process"""
    return app.send_static_file('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        # Get markdown content from request
        data = request.get_json()
        markdown_content = data.get('markdown')
        
        if not markdown_content:
            return jsonify({'error': 'No markdown content provided'}), 400

        # Create temporary file paths
        output_file = os.path.join(TEMP_DIR, 'presentation.pptx')

        # Convert markdown to PPT
        converter = MarkdownToPptConverter(markdown_content, output_file, mode=0)
        converter.convert()

        # Send the file
        return send_file(
            output_file,
            mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation',
            as_attachment=True,
            download_name='presentation.pptx'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up temporary files
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except:
                pass

if __name__ == '__main__':
    app.run(debug=True)