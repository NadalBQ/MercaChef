from flask import request, redirect, url_for, Flask, render_template
import os


csv_file_path = "./static/csvs/inventory.csv"
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No hay archivo", 400
    file = request.files['image']
    if file.filename == '':
        return "Nombre vacío", 400
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)