from flask import Flask
from datetime import datetime
import os
from database import db



def server():
    
    app = Flask(__name__)

    #For data base configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'INBest_cloud_for_humans'
    db.init_app(app) #Init database
    
    
    
    return app
