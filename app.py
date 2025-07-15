import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from main import process_image

app = Flask(__name__)

# Folder names
UPLOAD_FOLDER = 'static/input-images'
FINAL_OUTPUT_FOLDER = 'static/finall_output'

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FINAL_OUTPUT_FOLDER, exist_ok=True)

# Set config
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FINAL_OUTPUT_FOLDER'] = FINAL_OUTPUT_FOLDER

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', output_path=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)  # Save the uploaded image to the input folder

        # Process the image
        output_path = os.path.join(FINAL_OUTPUT_FOLDER, f'{os.path.splitext(filename)[0]}_enhanced.jpg')
        process_image(input_path, output_path)

        return render_template('index.html', output_path=output_path)
    else:
        return redirect(url_for('index'), output_path=None)

if __name__ == '__main__':
    app.run(debug=True)
