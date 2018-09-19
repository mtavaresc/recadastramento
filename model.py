from base import db


class Pegaso(db.Model):
    __tablename__ = "pegaso"
    __bind_by__ = "in"

    matricula = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    nis = db.Column(db.String(11))
    dtnascto = db.Column(db.String(11))


class Trabalhador(db.Model):
    __tablename__ = "trabalhador"
    __bind_key__ = "out"

    # Trabalhador
    cpfTrab = db.Column(db.String(11))
    nisTrab = db.Column(db.String(11))
    nmTrab = db.Column(db.String(70))
    sexo = db.Column(db.String(1))
    racaCor = db.Column(db.Integer)
    estCiv = db.Column(db.Integer)
    grauInstr = db.Column(db.String(2))
    indPriEmpr = db.Column(db.String(1))
    nmSoc = db.Column(db.String(70))
    # Nascimento
    dtNascto = db.Column(db.Date)
    codMunic = db.Column(db.Integer)
    uf = db.Column(db.String(2))
    paisNascto = db.Column(db.String(3))
    paisNac = db.Column(db.String(3))
    nmMae = db.Column(db.String(70))
    nmPai = db.Column(db.String(70))
    # CTPS
    nrCtpts = db.Column(db.String(11))
    serieCtps = db.Column(db.String(5))
    ufCtps = db.Column(db.String(2))
    # RIC
    nrRic = db.Column(db.String(14))
    ric_orgaoEmissor = db.Column(db.String(20))
    ric_dtExped = db.Column(db.Date)
    # RG
    nrRg = db.Column(db.String(14))
    rg_orgaoEmissor = db.Column(db.String(20))
    rg_dtExped = db.Column(db.Date)
    # RNE
    nrRne = db.Column(db.String(14))
    rne_orgaoEmissor = db.Column(db.String(20))
    rne_dtExped = db.Column(db.Date)
    # OC
    nrOc = db.Column(db.String(14))
    oc_orgaoEmissor = db.Column(db.String(20))
    oc_dtExped = db.Column(db.Date)
    oc_dtValid = db.Column(db.Date)

    db.PrimaryKeyConstraint(cpfTrab, nisTrab, dtNascto)

    def __init__(self, cpf, nis, nome, sexo, raca, est_civ, dtnascto):
        self.cpf = cpf
        self.nis = nis
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.est_civ = est_civ
        self.dtNascto = dtnascto
