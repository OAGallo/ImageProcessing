from config import server
from database import db
from Models import auth 

#To use routes
from routes.main_routes import main
from routes.auth_routes import auth as user_auth

app = server()
app.register_blueprint(main)
app.register_blueprint(user_auth)

auth.init_auth(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True, host="0.0.0.0")
