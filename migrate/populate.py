# coding=utf-8
from sqlalchemy import func

from models.formulario import Pegaso, User


def populate(app, db):
    with app.app_context():
        # PEGASUS
        db.session.add(Pegaso('031873', 'TAVARES', '03288866677', '123456', func.to_date('1991-01-01', 'YYYY-MM-DD')))
        db.session.add(Pegaso('123456', 'RECAD', '03288866677', '123456', func.to_date('1991-01-01', 'YYYY-MM-DD')))
        # FORM_LOGIN
        db.session.add(User('031873', 'MARCELO TAVARES', '0321991', adm=1))
        db.session.add(User('123456', 'SERVIDOR RECAD', '1231991'))
        db.session.commit()
