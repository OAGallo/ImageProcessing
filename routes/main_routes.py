from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from Models.imagesModel import Images
from database import db

import cv2 

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

#Image processing routes

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/Processing", methods=["GET", "POST"])
def processing():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = f"original_{filename}"
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # Guardar en la base de datos
            image = Images(filename=filename)
            db.session.add(image)
            db.session.commit()
            flash('Image uploaded successfully!')
            #return redirect(url_for('main.index'))
            return render_template("images/ProcessingMenu.html", filename=filename)
        else:
            flash('Invalid file type. Allowed formats (.png, .jpg, .jpeg, .gif)')
    return render_template("images/images.html")


@main.route("/savedImages")
def list_images():
    try:
        images = Images.query.all()
        if not images:
            message = "Don't have saved images"
        else:
            message = None
    except Exception as e:
        images = []
        message = "Data base or table doesn't exist"
    return render_template("images/list_saved_images.html", images=images)

@main.route('/uploads/<filename>')
def download_image(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

@main.route('/rotate_image', methods=['POST'])
def rotate_image():
    filename = request.form['filename']
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    img = cv2.imread(filepath)
    if img is not None:
        rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        processed_filename = f"rotated_{filename}"
        processed_path = os.path.join(UPLOAD_FOLDER, processed_filename)
        cv2.imwrite(processed_path, rotated)
        flash('Imagen rotada correctamente.')
        return render_template("images/ProcessingMenu.html", filename=processed_filename)
    else:
        flash('No se pudo procesar la imagen.')
        return redirect(url_for('main.processing'))
    
@main.route('/grayscale_image', methods=['POST'])
def grayscale_image():
    filename = request.form['filename']
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    img = cv2.imread(filepath)
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed_filename = f"gray_{filename}"
        processed_path = os.path.join(UPLOAD_FOLDER, processed_filename)
        cv2.imwrite(processed_path, gray)
        flash('Imagen convertida a escala de grises.')
        return render_template("images/ProcessingMenu.html", filename=processed_filename)
    else:
        flash('No se pudo procesar la imagen.')
        return redirect(url_for('main.processing'))
    
@main.route('/save_processed_image', methods=['POST'])
def save_processed_image():
    filename = request.form['filename']
    processed_filename = f"processed_{filename}"
    original_path = os.path.join(UPLOAD_FOLDER, filename)
    processed_path = os.path.join(UPLOAD_FOLDER, processed_filename)

    if not os.path.exists(processed_path):
        import shutil
        shutil.copyfile(original_path, processed_path)
    
    if Images.query.filter_by(filename=processed_filename).first():
        flash('The image is already saved.')
    else:
        image = Images(filename=processed_filename)
        db.session.add(image)
        db.session.commit()
        flash('Save processed image.')
    return render_template("images/ProcessingMenu.html", filename=processed_filename)