from base import db


class Lotacao(db.Model):
    __tablename__ = "tb_lota"
    __table_args__ = {'schema': 'zeus'}

    lot_cod = db.Column(db.CHAR(6), primary_key=True)
    lot_desc = db.Column(db.String(70))
    lot_sala = db.Column(db.String(11))
    lot_resp = db.Column(db.String(11))
    lot_obs = db.Column(db.String(11))
    usuario = db.Column(db.String(11))
    dtusu = db.Column(db.Date)
    trans = db.Column(db.String(11))
    lot_grupo = db.Column(db.String(11))
    lot_seq = db.Column(db.String(11))
    lot_texto = db.Column(db.String(11))
    lot_ativo = db.Column(db.String(11))
    lot_macro = db.Column(db.String(11))
    lot_lota = db.Column(db.String(11))


class CargoFuncao(db.Model):
    __tablename__ = "tb_carfun"
    __table_args__ = {'schema': 'zeus'}

    car_cod = db.Column(db.CHAR(6), primary_key=True)
    car_desc = db.Column(db.String(70))
    car_tipo = db.Column(db.CHAR(1))
    car_obs = db.Column(db.String(250))
    usuario = db.Column(db.String(70))
    dtusu = db.Column(db.Date)
    trans = db.Column(db.CHAR(1))
    car_ativo = db.Column(db.CHAR(1))


class HistoricoLotacao(db.Model):
    __tablename__ = "tb_hlota"
    __table_args__ = {'schema': 'zeus'}

    hlt_cod = db.Column(db.CHAR(6), primary_key=True)
    hlt_matr = db.Column(db.CHAR(6))
    hlt_lota = db.Column(db.CHAR(7))
    hlt_sit = db.Column(db.CHAR(1))
    hlt_dtmudou = db.Column(db.Date)
    hlt_motivo = db.Column(db.String(50))
    usuario = db.Column(db.String(70))
    dtusu = db.Column(db.Date)
    trans = db.Column(db.CHAR(1))
