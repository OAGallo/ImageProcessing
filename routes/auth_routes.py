from flask import Blueprint, render_template, request, redirect, url_for, flash
from Models.userModel import UserModel
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if UserModel.query.filter_by(name=name).first():
            flash('El usuario ya existe')
            return redirect(url_for('auth.register'))
        user = UserModel(
            name=name,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuario creado exitosamente')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = UserModel.query.filter_by(name=name).first()
        if user and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.id)
            flash('Login exitoso')
            # Puedes devolver el token o guardarlo en sesión/cookie según tu flujo
            return render_template('auth/login.html', token=access_token)
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('auth/login.html')