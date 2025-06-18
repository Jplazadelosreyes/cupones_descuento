# app/__init__.py

from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

def create_app():
    app = Flask(__name__)

    # Asigna la clave secreta desde las variables de entorno
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .routes import main
    app.register_blueprint(main)

    return app
