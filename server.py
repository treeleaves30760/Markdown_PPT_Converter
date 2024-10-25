from flask import Flask, request, send_file, jsonify
from src.converter.converter import MarkdownToPptConverter
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure temp directory for file operations
TEMP_DIR = tempfile.gettempdir()

@app.route('/api/healthcheck')
def healthcheck():
    return jsonify({"status": "healthy"})

@app.route('/convert', methods=['POST', 'OPTIONS'])
def convert():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    try:
        # Get markdown content from request
        data = request.get_json()
        markdown_content = data.get('markdown')
        
        if not markdown_content:
            return jsonify({'error': 'No markdown content provided'}), 400

        # Create temporary file paths
        temp_dir = tempfile.mkdtemp()
        output_file = os.path.join(temp_dir, 'presentation.pptx')

        # Convert markdown to PPT
        converter = MarkdownToPptConverter(markdown_content, output_file, mode=0)
        converter.convert()

        # Send the file
        response = send_file(
            output_file,
            mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation',
            as_attachment=True,
            download_name='presentation.pptx'
        )
        
        # Add CORS headers
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up temporary files
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
                os.rmdir(temp_dir)
            except:
                pass

if __name__ == '__main__':
    app.run(debug=True)