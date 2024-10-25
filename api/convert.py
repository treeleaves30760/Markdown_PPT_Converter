from flask import Flask, request, send_file, jsonify
from src.converter.converter import MarkdownToPptConverter
import os
import tempfile
import sys

# Add the parent directory to Python path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

def handle_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response

@app.route('/api/convert', methods=['POST', 'OPTIONS'])
def convert():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        return handle_cors(response)

    try:
        data = request.get_json()
        markdown_content = data.get('markdown')
        
        if not markdown_content:
            return jsonify({'error': 'No markdown content provided'}), 400

        temp_dir = tempfile.mkdtemp()
        output_file = os.path.join(temp_dir, 'presentation.pptx')

        converter = MarkdownToPptConverter(markdown_content, output_file, mode=0)
        converter.convert()

        response = send_file(
            output_file,
            mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation',
            as_attachment=True,
            download_name='presentation.pptx'
        )
        
        response = handle_cors(response)
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
                os.rmdir(temp_dir)
            except:
                pass

if __name__ == '__main__':
    app.run(debug=True)
