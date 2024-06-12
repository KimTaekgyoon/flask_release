import os
import json
from flask import Flask, request, jsonify
import functions
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/receive_string', methods=['POST'])
def receive_string():
    dto_json = request.get_json()
    response = json.dumps(dto_json, ensure_ascii=False)
    print(dto_json)
    return response

@app.route('/processImage', methods=['POST'])
def process_image():
    if 'imageFile' not in request.files:
        return jsonify({"error": "No image file found"}), 400

    image = request.files['imageFile']
    filename = secure_filename(image.filename)
    img_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(img_path)

    print(f"Image saved to {img_path}")

    labels, confidences = functions.yolo(img_path)

    try:
        os.remove(img_path)
    except Exception as e:
        print(f"Error removing file: {e}")

    response_data = {
        "labels": labels,
        "confidences": confidences
    }

    print(f"Response data: {response_data}")

    return jsonify(response_data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
