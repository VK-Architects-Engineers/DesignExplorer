from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the index.html file from the 'static' directory
    
    return send_from_directory('', 'index.html')

# This route will serve all other static files
@app.route('/<path:filename>')
def serve_static(filename):
    print(filename)
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run()
