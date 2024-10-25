from flask import Flask, request, send_file, jsonify
from src.converter.converter import MarkdownToPptConverter
import os
import tempfile

app = Flask(__name__)

# Configure temp directory for file operations
TEMP_DIR = tempfile.gettempdir()

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Markdown to PPT Converter</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
                textarea { width: 100%; height: 300px; margin: 1rem 0; }
                button { padding: 0.5rem 1rem; background: #007bff; color: white; border: none; cursor: pointer; }
                button:hover { background: #0056b3; }
            </style>
        </head>
        <body>
            <h1>Markdown to PPT Converter</h1>
            <textarea id="markdown" placeholder="Enter your Markdown here..."></textarea>
            <button onclick="convertToPPT()">Convert to PPT</button>
            <div id="status"></div>

            <script>
                async function convertToPPT() {
                    const markdown = document.getElementById('markdown').value;
                    const status = document.getElementById('status');
                    status.textContent = 'Converting...';
                    
                    try {
                        const response = await fetch('/convert', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ markdown }),
                        });
                        
                        if (response.ok) {
                            const blob = await response.blob();
                            const url = window.URL.createObjectURL(blob);
                            const a = document.createElement('a');
                            a.href = url;
                            a.download = 'presentation.pptx';
                            document.body.appendChild(a);
                            a.click();
                            window.URL.revokeObjectURL(url);
                            document.body.removeChild(a);
                            status.textContent = 'Conversion successful!';
                        } else {
                            status.textContent = 'Conversion failed. Please try again.';
                        }
                    } catch (error) {
                        status.textContent = 'Error: ' + error.message;
                    }
                }
            </script>
        </body>
    </html>
    '''

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

@app.route('/api/convert', methods=['POST'])
def api_convert():
    """API endpoint for programmatic access"""
    try:
        data = request.get_json()
        markdown_content = data.get('markdown')
        
        if not markdown_content:
            return jsonify({'error': 'No markdown content provided'}), 400

        output_file = os.path.join(TEMP_DIR, 'presentation.pptx')
        converter = MarkdownToPptConverter(markdown_content, output_file, mode=0)
        converter.convert()

        return send_file(
            output_file,
            mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation',
            as_attachment=True,
            download_name='presentation.pptx'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)