from flask import current_app

def add_all_commit(classe):
    session = current_app.db.session

    session.add(classe)
    session.commit()