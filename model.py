from app import db


class Colaborador(db.Model):
    __tablename__ = 'colaborador'

    cpf_trab = db.Column('cpfTrab', db.String(11))
    nis_trab = db.Column('nisTrab', db.String(11))
    nm_trab = db.Column('nmTrab', db.String(70))
