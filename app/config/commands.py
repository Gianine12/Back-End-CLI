from flask.cli import AppGroup
from flask import Flask
import click
from faker import Faker

fake = Faker()

from app.models.user_model import Users
from app.services.services import add_all_commit


def create_user(app: Flask):
    com_user = AppGroup("user")

    @com_user.command("create")
    @click.argument("quantidade")
    
    def user_create(quantidade: int):

        for u in range(int(quantidade)):

            user = {
               "login": fake.name()
            }
            password = fake.password()

            new_user = Users(**user)
            new_user.password = password

            add_all_commit(new_user)

    app.cli.add_command(com_user)

def init_app(app: Flask):
    create_user(app)