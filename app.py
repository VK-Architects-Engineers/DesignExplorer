from flask import Flask, send_from_directory, render_template, request
app = Flask(__name__)
import os
from dotenv import load_dotenv

load_dotenv()

@app.route('/')
def index():
    # Serve the index.html file from the 'static' directory

    root_url = os.environ.get("DOCUMENT_DATA_HOST")
    if not root_url:
        root_url = request.url_root
    
    document_uri = os.environ.get("DOCUMENT_DATA_URI", "designexplorer_data")
    
    return render_template('index.html', host=root_url, document_uri=document_uri)
    # return send_from_directory('', 'index.html')

# This route will serve all other static files
@app.route('/<path:filename>')
def serve_static(filename):
    # print(filename)
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run()
