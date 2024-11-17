#-*- coding:utf-8 -*-
from flask import Flask
from .routes import main_bp  # Importamos el blueprint de las rutas

def create_app():
    app = Flask(__name__)
    app.secret_key = 'c1b3rs3cur1ty_2024'

    # Registrar los blueprints
    app.register_blueprint(main_bp)

    return app