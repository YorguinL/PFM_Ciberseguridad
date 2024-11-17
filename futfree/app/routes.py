from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from email_validator import validate_email, EmailNotValidError
from connection import Connection

# Crear un blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return redirect(url_for("main.auth"))

@main_bp.route("/auth")
def auth():
    return render_template("auth/auth.html")

@main_bp.route("/auth/<provider>")
def auth_form(provider):
    return render_template(f"auth/{provider}.html")

@main_bp.route("/signup")
def signup():
    return render_template("auth/signup.html")

@main_bp.route("/login")
def login():
    return render_template("auth/login.html")

@main_bp.route("/submit", methods=['POST'])
def log_connection():

    # Obtener datos
    signup = True if request.form.get('form_id') == "signup" else False
    social = request.form.get("social")
    email = request.form.get('email')
    password = request.form.get('password')

    # Validar y sanitizar datos
    try:

        if email and password:
            validate_email(email)
            sanitized_password = sanitize_input(password)
            conn = Connection()

            if signup:
                if social is None:
                    
                    day = request.form.get("day")
                    month = request.form.get("month")
                    year = request.form.get("year")

                    if not is_adult(day, month, year):
                        flash("Debes ser mayor de 18 años para registrarte.")
                        return render_template("auth/signup.html")
                    
                    conn.connection_data(signup, social, email, sanitized_password)
                    return render_template("auth/login.html")
                else:
                    print(f'Registro desde {social}')
                    conn.connection_data(signup, social, email, sanitized_password) 
                    flash('Correo electrónico o contraseña incorrecto.', 'error')
                    return render_template(f"auth/{social}.html")
                
            else:
                print('Inicio de sesión')
                conn.connection_data(signup, social, email, sanitized_password)
                flash('Correo electrónico o contraseña incorrecto.', 'error')
                return render_template("auth/login.html")

    except EmailNotValidError:
        abort(400)