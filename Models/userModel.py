from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique= True, nullable=False)
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255), nullable=False)
    
    #Relation with images table:
    # 1:N (1 user can save N images)
    images = db.relationship('Images', backref='user', lazy=True)
    
    
    def __repr__(self):
        return f'User {self.name}'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def get_check_password(self, password):
        return check_password_hash(self.password_hash, password) 
    
    