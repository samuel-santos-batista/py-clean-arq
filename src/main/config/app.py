from flask import Flask
from src.main.routes import router_bp

app = Flask(__name__)

app.register_blueprint(router_bp)
