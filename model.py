from base import db


class Pegaso(db.Model):
    __tablename__ = "TV_CADASTRO"

    matricula = db.Column("MATR", db.CHAR(6), primary_key=True)
    nome = db.Column(db.String(70))
    cpf = db.Column(db.String(11))
    pispasep = db.Column(db.String(11))
    dtnasc = db.Column(db.Date)


class User(db.Model):
    __tablename__ = "FORM_LOGIN"

    matricula = db.Column(db.CHAR(6), primary_key=True)
    nome = db.Column(db.String(70))
    senha = db.Column(db.String(7))
    adm = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.matricula


class Trabalhador(db.Model):
    __tablename__ = "TRABALHADOR"

    matricula = db.Column(db.CHAR(6), primary_key=True)
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
    nrCtps = db.Column(db.String(11))
    serieCtps = db.Column(db.String(5))
    ufCtps = db.Column(db.String(2))
    # RG
    nrRg = db.Column(db.String(14))
    rg_orgaoEmissor = db.Column(db.String(20))
    rg_dtExped = db.Column(db.Date)
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
    # Info Deficiencia
    defFisica = db.Column(db.String(1))
    defVisual = db.Column(db.String(1))
    defAuditiva = db.Column(db.String(1))
    defMental = db.Column(db.String(1))
    defIntelectual = db.Column(db.String(1))
    defReadap = db.Column(db.String(1))
    infoCota = db.Column(db.String(1))
    observacao = db.Column(db.String(255))
    # Aposentadoria
    trabAposent = db.Column(db.String(1))
    # Contato
    fonePrinc = db.Column(db.String(13))
    foneAlternat = db.Column(db.String(13))
    emailPrinc = db.Column(db.String(60))
    emailAlternat = db.Column(db.String(60))

    protocolo = db.Column(db.String(14), unique=True)

    def __init__(self, matricula, cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr,
                 nm_soc, dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, nm_pai, nr_ctps, serie_ctps, uf_ctps,
                 nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor, oc_dt_exped, oc_dt_valid, nr_reg_cnh,
                 cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab, categoria_cnh, tp_lograd, dsc_lograd, nr_lograd,
                 complemento, bairro, cep, end_cod_munic, end_uf, def_fisica, def_visual, def_auditiva, def_mental,
                 def_intelectual, def_readap, info_cota, observacao, trab_aposent, fone_princ, fone_alternat,
                 email_princ, email_alternat, protocolo):
        self.matricula = matricula
        # Trabalhador
        self.cpfTrab = cpf_trab
        self.nisTrab = nis_trab
        self.nmTrab = nm_trab
        self.sexo = sexo
        self.racaCor = raca_cor
        self.estCiv = est_civ
        self.grauInstr = grau_instr
        self.indPriEmpr = ind_pri_empr
        self.nmSoc = nm_soc
        # Nascimento
        self.dtNascto = dt_nascto
        self.codMunic = cod_munic
        self.uf = uf
        self.paisNascto = pais_nascto
        self.paisNac = pais_nac
        self.nmMae = nm_mae
        self.nmPai = nm_pai
        # CTPS
        self.nrCtps = nr_ctps
        self.serieCtps = serie_ctps
        self.ufCtps = uf_ctps
        # RG
        self.nrRg = nr_rg
        self.rg_orgaoEmissor = rg_orgao_emissor
        self.rg_dtExped = rg_dt_exped
        # OC
        self.nrOc = nr_oc
        self.oc_orgaoEmissor = oc_orgao_emissor
        self.oc_dtExped = oc_dt_exped
        self.oc_dtValid = oc_dt_valid
        # CNH
        self.nrRegCnh = nr_reg_cnh
        self.cnh_dtExped = cnh_dt_exped
        self.ufCnh = uf_cnh
        self.cnh_dtValid = cnh_dt_valid
        self.dtPriHab = dt_pri_hab
        self.categoriaCnh = categoria_cnh
        # Endereco - Brasil
        self.tpLograd = tp_lograd
        self.dscLograd = dsc_lograd
        self.nrLograd = nr_lograd
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.end_codMunic = end_cod_munic
        self.end_uf = end_uf
        # Info Deficiencia
        self.defFisica = def_fisica
        self.defVisual = def_visual
        self.defAuditiva = def_auditiva
        self.defMental = def_mental
        self.defIntelectual = def_intelectual
        self.defReadap = def_readap
        self.infoCota = info_cota
        self.observacao = observacao
        # Aposentadoria
        self.trabAposent = trab_aposent
        # Contato
        self.fonePrinc = fone_princ
        self.foneAlternat = fone_alternat
        self.emailPrinc = email_princ
        self.emailAlternat = email_alternat
        # Protocolo
        self.protocolo = protocolo


class Dependentes(db.Model):
    __tablename__ = "DEPENDENTES"

    matrTab = db.Column(db.CHAR(6))
    tpDep = db.Column(db.String(2))
    nmDep = db.Column(db.String(70))
    dep_dtNascto = db.Column(db.Date)
    cpfDep = db.Column(db.String(11))
    depIRRF = db.Column(db.String(1))
    depSF = db.Column(db.String(1))
    incTrab = db.Column(db.String(1))
    db.PrimaryKeyConstraint(matrTab, cpfDep, name="dep_pk")

    def __init__(self, matr_tab, tp_dep, nm_dep, dep_dt_nascto, cpf_dep, dep_irrf, dep_sf, inc_trab):
        self.matrTab = matr_tab
        self.tpDep = tp_dep
        self.nmDep = nm_dep
        self.dep_dtNascto = dep_dt_nascto
        self.cpfDep = cpf_dep
        self.depIRRF = dep_irrf
        self.depSF = dep_sf
        self.incTrab = inc_trab


class Paises(db.Model):
    __tablename__ = "PAISES"

    codigo = db.Column(db.String(3), primary_key=True)
    nome = db.Column(db.String(100))

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Estados(db.Model):
    __tablename__ = "ESTADOS"

    uf = db.Column(db.CHAR(2), primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, uf, nome):
        self.uf = uf
        self.nome = nome


class Municipios(db.Model):
    __tablename__ = "MUNICIPIOS"

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    uf = db.Column(db.CHAR(2))

    def __init__(self, codigo, nome, uf):
        self.codigo = codigo
        self.nome = nome
        self.uf = uf


class Bairros(db.Model):
    __tablename__ = "BAIRROS"

    codigo = db.Column(db.CHAR(10), primary_key=True)
    nome = db.Column(db.String(70))
    municipio = db.Column(db.String(70))
    uf = db.Column(db.CHAR(2))

    def __init__(self, codigo, nome, municipio, uf):
        self.codigo = codigo
        self.nome = nome
        self.municipio = municipio
        self.uf = uf


class TiposLogradouro(db.Model):
    __tablename__ = "TIPOS_LOGRADOURO"

    codigo = db.Column(db.CHAR(4), primary_key=True)
    nome = db.Column(db.String(30))

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
