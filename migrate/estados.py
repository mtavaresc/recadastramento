# coding=utf-8
from models.formulario import Estados


def migrate_estados(app, db):
    with app.app_context():
        db.session.add(Estados("AC", "Acre"))
        db.session.add(Estados("AL", "Alagoas"))
        db.session.add(Estados("AM", "Amazonas"))
        db.session.add(Estados("AP", "Amapá"))
        db.session.add(Estados("BA", "Bahia"))
        db.session.add(Estados("CE", "Ceará"))
        db.session.add(Estados("DF", "Distrito Federal"))
        db.session.add(Estados("ES", "Espírito Santo"))
        db.session.add(Estados("GO", "Goiás"))
        db.session.add(Estados("MA", "Maranhão"))
        db.session.add(Estados("MG", "Minas Gerais"))
        db.session.add(Estados("MS", "Mato Grosso do Sul"))
        db.session.add(Estados("MT", "Mato Grosso"))
        db.session.add(Estados("PA", "Pará"))
        db.session.add(Estados("PB", "Paraíba"))
        db.session.add(Estados("PE", "Pernambuco"))
        db.session.add(Estados("PI", "Piauí"))
        db.session.add(Estados("PR", "Paraná"))
        db.session.add(Estados("RJ", "Rio de Janeiro"))
        db.session.add(Estados("RN", "Rio Grande do Norte"))
        db.session.add(Estados("RO", "Rondônia"))
        db.session.add(Estados("RR", "Roraima"))
        db.session.add(Estados("RS", "Rio Grande do Sul"))
        db.session.add(Estados("SC", "Santa Catarina"))
        db.session.add(Estados("SE", "Sergipe"))
        db.session.add(Estados("SP", "São Paulo"))
        db.session.add(Estados("TO", "Tocantins"))
        db.session.commit()
