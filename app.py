from flask import Flask, request, render_template
import logging
import pytesseract
from PIL import Image
import os
import uuid

app = Flask(__name__)

# Create a log handler for the app logger
handler = logging.FileHandler('log.log')
handler.setLevel(logging.DEBUG)

# Create a formatter for the log handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the log handler to the app logger
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    filename = str(uuid.uuid4()) + ".jpeg"
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    file.save(os.path.join("uploads", filename))
    image = Image.open(os.path.join("uploads", filename))
    text = pytesseract.image_to_string(image)
    app.logger.debug(f'Image uploaded: {os.path.join("uploads", filename)}')
    app.logger.debug(f'Text extracted from image: {text}')
    return render_template('output.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
