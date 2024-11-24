
from flask import Flask, render_template
from .routes import main_bp  # Importamos el blueprint de las rutas

def create_app():
    app = Flask(__name__)
    app.secret_key = 'c1b3rs3cur1ty_2024'

    # Registrar los blueprints
    app.register_blueprint(main_bp)

    # Manejadores de errores
    @app.errorhandler(400)
    def bad_request_error(error):
        return render_template('error/400.html'), 400

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/404.html'), 404

    return app