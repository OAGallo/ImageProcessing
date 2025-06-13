from database import db
from datetime import datetime

class Images(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    filename = db.Column(db.String(200), nullable = False)
    
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f'<Image {self.filename}>'
