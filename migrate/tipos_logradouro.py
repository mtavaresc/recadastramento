# coding=utf-8
from models.formulario import TiposLogradouro


def migrate_tipos_logradouro(app, db):
    with app.app_context():
        db.session.add(TiposLogradouro("AL", "Alameda"))
        db.session.add(TiposLogradouro("AV", "Avenida"))
        db.session.add(TiposLogradouro("BAL", "Balneário"))
        db.session.add(TiposLogradouro("BL", "Bloco"))
        db.session.add(TiposLogradouro("CH", "Chácara"))
        db.session.add(TiposLogradouro("CJ", "Conjunto"))
        db.session.add(TiposLogradouro("COND", "Condomínio"))
        db.session.add(TiposLogradouro("EST", "Estrada"))
        db.session.add(TiposLogradouro("FAZ", "Fazenda"))
        db.session.add(TiposLogradouro("GAL", "Galeria"))
        db.session.add(TiposLogradouro("GJA", "Granja"))
        db.session.add(TiposLogradouro("JD", "Jardim"))
        db.session.add(TiposLogradouro("LG", "Largo"))
        db.session.add(TiposLogradouro("LOT", "loteamento"))
        db.session.add(TiposLogradouro("PÇ", "Praça"))
        db.session.add(TiposLogradouro("PR", "Praia"))
        db.session.add(TiposLogradouro("PRQ", "Parque"))
        db.session.add(TiposLogradouro("Q", "Quadra"))
        db.session.add(TiposLogradouro("R", "Rua"))
        db.session.add(TiposLogradouro("ST", "Setor"))
        db.session.add(TiposLogradouro("TV", "Travessa"))
        db.session.add(TiposLogradouro("VL", "Vila"))
        db.session.commit()
