from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permite peticiones de otros dominios (React)
    
    from .routes import api
    app.register_blueprint(api)  # Registra las rutas

    return app
