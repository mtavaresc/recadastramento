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
    # CNH
    nrRegCnh = db.Column(db.String(12))
    cnh_dtExped = db.Column(db.Date)
    ufCnh = db.Column(db.String(2))
    cnh_dtValid = db.Column(db.Date)
    dtPriHab = db.Column(db.Date)
    categoriaCnh = db.Column(db.String(2))
    # Endereco - Brasil
    tpLograd = db.Column(db.String(4))
    dscLograd = db.Column(db.String(80))
    nrLograd = db.Column(db.String(10))
    complemento = db.Column(db.String(30))
    bairro = db.Column(db.String(60))
    cep = db.Column(db.String(8))
    end_codMunic = db.Column(db.Integer)
    end_uf = db.Column(db.String(2))
    # Endereco - Exterior
    paisResid = db.Column(db.String(3))
    ext_dscLograd = db.Column(db.String(80))
    ext_nrLograd = db.Column(db.String(10))
    ext_complemento = db.Column(db.String(30))
    ext_bairro = db.Column(db.String(60))
    nmCid = db.Column(db.String(50))
    codPostal = db.Column(db.String(12))
    # Estrangeiro
    dtChegada = db.Column(db.Date)
    classTrabEstran = db.Column(db.Integer)
    casadoBr = db.Column(db.String(1))
    filhosBr = db.Column(db.String(1))
    # Info Deficiencia
    defFisica = db.Column(db.String(1))
    defVisual = db.Column(db.String(1))
    defAuditiva = db.Column(db.String(1))
    defMental = db.Column(db.String(1))
    defIntelectual = db.Column(db.String(1))
    defReadap = db.Column(db.String(1))
    infoCota = db.Column(db.String(1))
    observacao = db.Column(db.String(255))
    # Dependete
    tpDep = db.Column(db.String(2))
    nmDep = db.Column(db.String(70))
    dep_dtNascto = db.Column(db.Date)
    cpfDep = db.Column(db.String(11))
    depIRRF = db.Column(db.String(1))
    depSF = db.Column(db.String(1))
    incTrab = db.Column(db.String(1))
    # Aposentadoria
    trabAposent = db.Column(db.String(1))
    # Contato
    fonePrinc = db.Column(db.String(13))
    foneAlternat = db.Column(db.String(13))
    emailPrinc = db.Column(db.String(60))
    emailAlternat = db.Column(db.String(60))

    db.PrimaryKeyConstraint(cpfTrab, nisTrab, dtNascto)

    def __init__(self, cpf, nis, nome, sexo, raca, est_civ, dtnascto):
        self.cpf = cpf
        self.nis = nis
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.est_civ = est_civ
        self.dtNascto = dtnascto
