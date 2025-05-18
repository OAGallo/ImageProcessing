from flask import Flask
from database import db
import secrets



def server():
    
    app = Flask(__name__)

    #For data base configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    db.init_app(app) #Init database
    
    
    return app
