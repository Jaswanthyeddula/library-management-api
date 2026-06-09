from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()
def create_app():
    app=Flask(__name__)
    app.json.sort_keys = False
    app.config.from_object('config.Config')

    db.init_app(app)
    JWTManager(app)
    bcrypt.init_app(app)
    from app.library_routes import book_bp
    app.register_blueprint(book_bp)
    from app.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    return app