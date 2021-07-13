from flask import Flask
from environs import Env

from app.config import migration, database, commands, command_admin

env = Env()
env.read_env()

def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database.init_app(app)
    migration.init_app(app)
    commands.init_app(app)
    command_admin.init_app(app)

    return app