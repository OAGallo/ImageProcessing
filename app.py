from config import server
from database import db

#To use routes
from routes.main_routes import main

app = server()
app.register_blueprint(main)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)
