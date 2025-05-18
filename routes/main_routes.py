from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from Models import imagesModel
from database import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/Userlogin", methods=['GET', 'POST'])
def userLogin():
    return render_template("auth/login.html")


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
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # Guardar en la base de datos
            image = imagesModel(filename=filename)
            db.session.add(image)
            db.session.commit()
            flash('Image uploaded successfully!')
            return redirect(url_for('main.index'))
    return render_template("images/images.html")


@main.route("/savedImages")
def list_images():
    try:
        images = imagesModel.query.all()
        if not images:
            message = "Don't have saved images"
        else:
            message = None
    except Exception as e:
        images = []
        message = "Data base or table doesn't exist"
    return render_template("images/list_saved_images.html", images=images)