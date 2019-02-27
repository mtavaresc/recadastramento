from base import db


class Lotacao(db.Model):
    __tablename__ = "TB_LOTA"

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
