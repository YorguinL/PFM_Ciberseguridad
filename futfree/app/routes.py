from flask import Blueprint, render_template, redirect, url_for, request, flash, abort

# Crear un blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def hello():
    return 'Hello, World!'