from base import db


class User(db.Model):
    __tablename__ = "form_login"

    matricula = db.Column(db.CHAR(6), primary_key=True)
    nome = db.Column(db.String(70))
    senha = db.Column(db.String(7))
    adm = db.Column(db.Integer)

    def __repr__(self):
        return '<user %r>' % self.matricula

    def __init__(self, matricula, nome, senha, adm=0):
        self.matricula = matricula
        self.nome = nome.upper()
        self.senha = senha
        self.adm = adm
