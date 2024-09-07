from flask import Flask, render_template, request, send_file
import requests
import io
from PIL import Image

app = Flask(__name__)

REMOVE_BG_API_KEY = 'tnrhPxi4fWP1GCKMXuqaKmwr'

def remove_background_with_api(image):
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    headers = {
        'X-Api-Key': REMOVE_BG_API_KEY,
    }
    files = {
        'image_file': buffer,
    }

    try:
        response = requests.post('https://api.remove.bg/v1.0/removebg', headers=headers, files=files)
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content))
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        img = Image.open(file.stream)
        result = remove_background_with_api(img)
        
        if result:
            img_io = io.BytesIO()
            result.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='output_image.png')
        else:
            return 'Background removal failed'

if __name__ == '__main__':
    app.run(debug=True)
