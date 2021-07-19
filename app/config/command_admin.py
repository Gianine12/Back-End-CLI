from flask.cli import AppGroup
from flask import Flask
import click
from faker import Faker

fake = Faker()

from app.models.user_model import Users
from app.services.services import add_all_commit


def create_admin(app: Flask):
    cli_admin = AppGroup("admin")
    
    @cli_admin.command("create")

    def create():
        admin = {
            "login" : fake.name(),
            "is_admin" : True
        }
        password = fake.password()
        new_user = Users(**admin)
        new_user.password = password

        add_all_commit(new_user)

        click.echo(f"Admin criado!!")
        click.echo(f"login: {new_user.login}")
        click.echo(f"password: {admin['password_has']}")

    app.cli.add_command(cli_admin)


def init_app(app: Flask):
    create_admin(app)