from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    cors_origins = os.environ.get('CORS_ORIGINS', '')
    print(f"CORS_ORIGINS environment variable: {cors_origins}")
    originsCors = cors_origins.split(',')
    print(f"Parsed CORS_ORIGINS: {originsCors}")

    CORS(app, origins=originsCors, supports_credentials=True)

    from app.routes.authRoute import bp as auth_bp
    from app.routes.taskRoute import bp as task_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app
