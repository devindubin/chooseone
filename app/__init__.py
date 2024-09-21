from flask import Flask
from .settings import bp as settings_blueprint
from .game import bp as games_blueprint
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(settings_blueprint)
app.register_blueprint(games_blueprint)