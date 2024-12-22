from flask import Flask, request, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__, static_folder="static")
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    url = data.get("url")
    keywords = data.get("keywords")
    if not url or not keywords:
        return jsonify({"error": "Both 'url' and 'keywords' are required"}), 400
    # Placeholder response for testing
    return jsonify({"url": url, "summary": "This is a test summary."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
