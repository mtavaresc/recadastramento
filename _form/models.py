from base import db


class Pegaso(db.Model):
    __tablename__ = "tv_cadastro"

    matr = db.Column(db.CHAR(6), primary_key=True)
    nome = db.Column(db.String(70))
    cpf = db.Column(db.String(11))
    pispasep = db.Column(db.String(11))
    dtnasc = db.Column(db.Date)

    def __init__(self, matr, nome, cpf, pispasep, dtnasc):
        self.matr = matr
        self.nome = nome.upper()
        self.cpf = cpf
        self.pispasep = pispasep
        self.dtnasc = dtnasc


class Trabalhador(db.Model):
    __tablename__ = "trabalhador"

    matricula = db.Column(db.CHAR(6), primary_key=True)
    # trabalhador
    cpftrab = db.Column(db.String(11))
    nistrab = db.Column(db.String(11))
    nmtrab = db.Column(db.String(70))
    sexo = db.Column(db.String(1))
    racacor = db.Column(db.Integer)
    estciv = db.Column(db.Integer)
    grauinstr = db.Column(db.String(2))
    indpriempr = db.Column(db.String(1))
    nmsoc = db.Column(db.String(70))
    # nascimento
    dtnascto = db.Column(db.Date)
    codmunic = db.Column(db.Integer)
    uf = db.Column(db.String(2))
    paisnascto = db.Column(db.String(3))
    paisnac = db.Column(db.String(3))
    nmmae = db.Column(db.String(70))
    cpfmae = db.Column(db.String(11))
    nmpai = db.Column(db.String(70))
    cpfpai = db.Column(db.String(11))
    # ctps
    nrctps = db.Column(db.String(11))
    seriectps = db.Column(db.String(5))
    ufctps = db.Column(db.String(2))
    # rg
    nrrg = db.Column(db.String(14))
    rg_orgaoemissor = db.Column(db.String(20))
    rg_dtexped = db.Column(db.Date)
    # oc
    nroc = db.Column(db.String(14))
    oc_orgaoemissor = db.Column(db.String(20))
    oc_dtexped = db.Column(db.Date)
    oc_dtvalid = db.Column(db.Date)
    # cnh
    nrregcnh = db.Column(db.String(12))
    cnh_dtexped = db.Column(db.Date)
    ufcnh = db.Column(db.String(2))
    cnh_dtvalid = db.Column(db.Date)
    dtprihab = db.Column(db.Date)
    categoriacnh = db.Column(db.String(2))
    # endereco - brasil
    tplograd = db.Column(db.String(4))
    dsclograd = db.Column(db.String(80))
    nrlograd = db.Column(db.String(10))
    complemento = db.Column(db.String(30))
    bairro = db.Column(db.String(60))
    cep = db.Column(db.String(8))
    end_codmunic = db.Column(db.Integer)
    end_uf = db.Column(db.String(2))
    # info deficiencia
    deffisica = db.Column(db.String(1))
    defvisual = db.Column(db.String(1))
    defauditiva = db.Column(db.String(1))
    defmental = db.Column(db.String(1))
    defintelectual = db.Column(db.String(1))
    defreadap = db.Column(db.String(1))
    infocota = db.Column(db.String(1))
    observacao = db.Column(db.String(255))
    # aposentadoria
    trabaposent = db.Column(db.String(1))
    # contato
    foneprinc = db.Column(db.String(13))
    fonealternat = db.Column(db.String(13))
    emailprinc = db.Column(db.String(60))
    emailalternat = db.Column(db.String(60))

    protocolo = db.Column(db.String(14))

    def __init__(self, matricula, cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr,
                 nm_soc, dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, cpf_mae, nm_pai, cpf_pai, nr_ctps,
                 serie_ctps, uf_ctps, nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor, oc_dt_exped,
                 oc_dt_valid, nr_reg_cnh, cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab, categoria_cnh, tp_lograd,
                 dsc_lograd, nr_lograd, complemento, bairro, cep, end_cod_munic, end_uf, def_fisica, def_visual,
                 def_auditiva, def_mental, def_intelectual, def_readap, info_cota, observacao, trab_aposent, fone_princ,
                 fone_alternat, email_princ, email_alternat, protocolo):
        self.matricula = matricula
        # trabalhador
        self.cpftrab = cpf_trab
        self.nistrab = nis_trab
        self.nmtrab = nm_trab
        self.sexo = sexo
        self.racacor = raca_cor
        self.estciv = est_civ
        self.grauinstr = grau_instr
        self.indpriempr = ind_pri_empr
        self.nmsoc = nm_soc
        # nascimento
        self.dtnascto = dt_nascto
        self.codmunic = cod_munic
        self.uf = uf
        self.paisnascto = pais_nascto
        self.paisnac = pais_nac
        self.nmmae = nm_mae
        self.cpfmae = cpf_mae
        self.nmpai = nm_pai
        self.cpfpai = cpf_pai
        # ctps
        self.nrctps = nr_ctps
        self.seriectps = serie_ctps
        self.ufctps = uf_ctps
        # rg
        self.nrrg = nr_rg
        self.rg_orgaoemissor = rg_orgao_emissor
        self.rg_dtexped = rg_dt_exped
        # oc
        self.nroc = nr_oc
        self.oc_orgaoemissor = oc_orgao_emissor
        self.oc_dtexped = oc_dt_exped
        self.oc_dtvalid = oc_dt_valid
        # cnh
        self.nrregcnh = nr_reg_cnh
        self.cnh_dtexped = cnh_dt_exped
        self.ufcnh = uf_cnh
        self.cnh_dtvalid = cnh_dt_valid
        self.dtprihab = dt_pri_hab
        self.categoriacnh = categoria_cnh
        # endereco - brasil
        self.tplograd = tp_lograd
        self.dsclograd = dsc_lograd
        self.nrlograd = nr_lograd
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.end_codmunic = end_cod_munic
        self.end_uf = end_uf
        # info deficiencia
        self.deffisica = def_fisica
        self.defvisual = def_visual
        self.defauditiva = def_auditiva
        self.defmental = def_mental
        self.defintelectual = def_intelectual
        self.defreadap = def_readap
        self.infocota = info_cota
        self.observacao = observacao
        # aposentadoria
        self.trabaposent = trab_aposent
        # contato
        self.foneprinc = fone_princ
        self.fonealternat = fone_alternat
        self.emailprinc = email_princ
        self.emailalternat = email_alternat
        # protocolo
        self.protocolo = protocolo


class Dependentes(db.Model):
    __tablename__ = "dependentes"

    matrtab = db.Column(db.CHAR(6))
    tpdep = db.Column(db.String(2))
    nmdep = db.Column(db.String(70))
    dep_dtnascto = db.Column(db.Date)
    cpfdep = db.Column(db.String(11))
    depirrf = db.Column(db.String(1))
    depsf = db.Column(db.String(1))
    inctrab = db.Column(db.String(1))
    db.PrimaryKeyConstraint(matrtab, cpfdep, name="dep_pk")

    def __init__(self, matr_tab, tp_dep, nm_dep, dep_dt_nascto, cpf_dep, dep_irrf, dep_sf, inc_trab):
        self.matrtab = matr_tab
        self.tpdep = tp_dep
        self.nmdep = nm_dep
        self.dep_dtnascto = dep_dt_nascto
        self.cpfdep = cpf_dep
        self.depirrf = dep_irrf
        self.depsf = dep_sf
        self.inctrab = inc_trab


class Documentos(db.Model):
    __tablename__ = "documentos"

    matrtab = db.Column(db.CHAR(6), primary_key=True)

    def __init__(self, matr_tab):
        self.matrtab = matr_tab


class Auditoria(db.Model):
    __tablename__ = "auditoria"

    matradm = db.Column(db.CHAR(6))
    matricula = db.Column(db.CHAR(6))
    action = db.Column(db.String(50))
    created = db.Column(db.DateTime, primary_key=True)

    def __init__(self, matradm, matricula, action, created):
        self.matradm = matradm
        self.matricula = matricula
        self.action = action
        self.created = created


class Paises(db.Model):
    __tablename__ = "paises"

    codigo = db.Column(db.String(3), primary_key=True)
    nome = db.Column(db.String(100))

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Estados(db.Model):
    __tablename__ = "estados"

    uf = db.Column(db.CHAR(2), primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, uf, nome):
        self.uf = uf
        self.nome = nome


class Municipios(db.Model):
    __tablename__ = "municipios"

    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    uf = db.Column(db.CHAR(2))

    def __init__(self, codigo, nome, uf):
        self.codigo = codigo
        self.nome = nome
        self.uf = uf


class Bairros(db.Model):
    __tablename__ = "bairros"

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
    __tablename__ = "tipos_logradouro"

    codigo = db.Column(db.CHAR(4), primary_key=True)
    nome = db.Column(db.String(30))

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
