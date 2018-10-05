# -*- coding: UTF-8 -*-
from flask import render_template, request, redirect, url_for
from datetime import date
from base import app, db


@app.route("/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")

        pegaso = db.session.execute(
            "SELECT nome FROM esocial.form_login WHERE matricula = '{}' AND senha = '{}'".format(matricula,
                                                                                                 senha)).count()
        form = db.session.execute(
            "SELECT protocolo FROM esocial.trabalhador WHERE matricula = '{}'".format(matricula))

        if pegaso > 0:
            if form.count() == 1:
                return render_template("reject.html", protocolo=form.first().protocolo)
            else:
                return redirect(url_for("recadastrar", matricula=matricula))
        else:
            return render_template("noauth.html")

    return render_template("auth.html")


@app.route("/<matricula>", methods=["GET", "POST"])
def recadastrar(matricula):
    if request.method == "POST":
        # Trabalhador
        cpf_trab = request.form.get("cpfTrab")
        cpf_trab = "".join(c for c in str(cpf_trab) if c not in ".-")
        nis_trab = request.form.get("nisTrab")
        nis_trab = "".join(c for c in str(nis_trab) if c not in ".-")
        nm_trab = request.form.get("nmTrab")
        sexo = request.form.get("sexo")
        raca_cor = request.form.get("racaCor")
        est_civ = request.form.get("estCiv")
        grau_instr = request.form.get("grauInstr")
        ind_pri_empr = request.form.get("indPriEmpr")
        nm_soc = request.form.get("nmSoc")
        # Nascimento
        dt_nascto = request.form.get("dtNascto")
        cod_munic = request.form.get("codMunic")
        uf = request.form.get("uf")
        pais_nascto = request.form.get("paisNascto")
        pais_nac = request.form.get("paisNac")
        nm_mae = request.form.get("nmMae")
        nm_pai = request.form.get("nmPai")
        # CTPS
        nr_ctps = request.form.get("nrCtps")
        serie_ctps = request.form.get("serieCtps")
        uf_ctps = request.form.get("ufCtps")
        # RG
        nr_rg = request.form.get("nrRg")
        rg_orgao_emissor = request.form.get("rg_orgaoEmissor")
        rg_dt_exped = request.form.get("rg_dtExped")
        # OC
        nr_oc = request.form.get("nrOc")
        oc_orgao_emissor = request.form.get("oc_orgaoEmissor")
        oc_orgao_emissor = oc_orgao_emissor.upper()
        oc_dt_exped = "" if request.form.get("oc_dtExped") is "" or request.form.get(
            "oc_dtExped") is None else request.form.get("oc_dtExped")
        oc_dt_valid = "" if request.form.get("oc_dtValid") is "" or request.form.get(
            "oc_dtValid") is None else request.form.get("oc_dtValid")
        # CNH
        nr_reg_cnh = request.form.get("nrRegCnh")
        cnh_dt_exped = "" if request.form.get("cnh_dtExped") is "" or request.form.get(
            "cnh_dtExped") is None else request.form.get("cnh_dtExped")
        uf_cnh = request.form.get("ufCnh")
        cnh_dt_valid = "" if request.form.get("cnh_dtValid") is "" or request.form.get(
            "cnh_dtValid") is None else request.form.get("cnh_dtValid")
        dt_pri_hab = "" if request.form.get("dtPriHab") is "" or request.form.get(
            "dtPriHab") is None else request.form.get("dtPriHab")
        categoria_cnh = request.form.get("categoriaCnh")
        # Endereco - Brasil
        tp_lograd = request.form.get("tpLograd")
        dsc_lograd = request.form.get("dscLograd")
        nr_lograd = request.form.get("nrLograd")
        complemento = request.form.get("complemento")
        bairro = request.form.get("bairro")
        cep = request.form.get("cep")
        cep = "".join(c for c in str(cep) if c not in "-")
        end_cod_munic = request.form.get("end_codMunic")
        end_uf = request.form.get("end_uf")
        # Endereco - Exterior
        pais_resid = request.form.get("paisResid")
        ext_dsc_lograd = request.form.get("ext_dscLograd")
        ext_nr_lograd = request.form.get("ext_nrLograd")
        ext_complemento = request.form.get("ext_complemento")
        ext_bairro = request.form.get("ext_bairro")
        nm_cid = request.form.get("nmCid")
        cod_postal = request.form.get("codPostal")
        # Info Deficiencia
        def_fisica = request.form.get("defFisica")
        def_visual = request.form.get("defVisual")
        def_auditiva = request.form.get("defAuditiva")
        def_mental = request.form.get("defMental")
        def_intelectual = request.form.get("defIntelectual")
        def_readap = request.form.get("defReadap")
        info_cota = request.form.get("infoCota")
        observacao = request.form.get("observacao")
        # Dependete
        tp_dep = request.form.get("tpDep")
        nm_dep = request.form.get("nmDep")
        dep_dt_nascto = "" if request.form.get("dep_dtNascto") is "" or request.form.get(
            "dep_dtNascto") is None else request.form.get("dep_dtNascto")
        cpf_dep = request.form.get("cpfDep")
        cpf_dep = "".join(c for c in str(cpf_dep) if c not in ".-")
        dep_irrf = request.form.get("depIRRF")
        dep_sf = request.form.get("depSF")
        inc_trab = request.form.get("incTrab")
        # Aposentadoria
        trab_aposent = request.form.get("trabAposent")
        # Contato
        fone_princ = request.form.get("fonePrinc")
        fone_princ = "".join(c for c in str(fone_princ) if c not in "()- ")
        fone_alternat = request.form.get("foneAlternat")
        fone_alternat = "".join(c for c in str(fone_alternat) if c not in "()- ")
        email_princ = request.form.get("emailPrinc")
        email_alternat = request.form.get("emailAlternat")

        protocolo = matricula + date.today().strftime("%Y%m%d")

        db.session.execute(
            "INSERT INTO esocial.trabalhador (matricula, cpfTrab, nisTrab, nmTrab, sexo, racaCor, estCiv, grauInstr, "
            "indPriEmpr, nmSoc, dtNascto, codMunic, uf, paisNascto, paisNac, nmMae, nmPai, nrCtps, serieCtps, ufCtps, "
            "nrRg, rg_orgaoEmissor, rg_dtExped, nrOc, oc_orgaoEmissor, oc_dtExped, oc_dtValid, nrRegCnh, cnh_dtExped, ufCnh, "
            "cnh_dtValid, dtPriHab, categoriaCnh, tpLograd, dscLograd, nrLograd, complemento, bairro, cep, end_codMunic, "
            "end_uf, paisResid, ext_dscLograd, ext_nrLograd, ext_complemento, ext_bairro, nmCid, codPostal, defFisica, "
            "defVisual, defAuditiva, defMental, defIntelectual, defReadap, infoCota, observacao, tpDep, nmDep, dep_dtNascto, "
            "cpfDep, depIRRF, depSF, incTrab, trabAposent, fonePrinc, foneAlternat, emailPrinc, emailAlternat) "
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                matricula, cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr, nm_soc,
                dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, nm_pai, nr_ctps, serie_ctps, uf_ctps,
                nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor, oc_dt_exped, oc_dt_valid,
                nr_reg_cnh, cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab, categoria_cnh, tp_lograd,
                dsc_lograd, nr_lograd, complemento, bairro, cep, end_cod_munic, end_uf, pais_resid,
                ext_dsc_lograd, ext_nr_lograd, ext_complemento, ext_bairro, nm_cid, cod_postal, def_fisica,
                def_visual, def_auditiva, def_mental, def_intelectual, def_readap, info_cota, observacao,
                tp_dep, nm_dep, dep_dt_nascto, cpf_dep, dep_irrf, dep_sf, inc_trab, trab_aposent, fone_princ,
                fone_alternat, email_princ, email_alternat, protocolo))
        db.session.commit()

        return render_template("submit.html", protocolo=protocolo)
    else:
        form = db.session.execute("SELECT protocolo FROM esocial.trabalhador WHERE matricula = '{}'".format(matricula))

        if form.count() == 1:
            return render_template("reject.html", protocolo=form.first().protocolo)
        else:
            # Campos preenchidos através da matricula do Pegaso
            pegaso = db.session.execute(
                "SELECT matr, nome, cpf, pispasep, TO_CHAR(dtnasc, 'YYYY-MM-DD') as dtnasc "
                "FROM zeus.tv_cadastro WHERE matr = '{}'".format(matricula)).first()

            # Selecionando paises
            cod_paises = [row[0] for row in db.session.execute("SELECT codigo FROM esocial.paises")]
            nome_paises = [row[0] for row in db.session.execute("SELECT nome FROM esocial.paises")]
            paises = dict(zip(cod_paises, nome_paises))

            # Selecionando estados
            uf_estados = [row[0] for row in db.session.execute("SELECT uf FROM esocial.estados")]
            nome_estados = [row[0] for row in db.session.execute("SELECT nome FROM esocial.estados")]
            estados = dict(zip(uf_estados, nome_estados))

            # Selecionando municipios
            cod_municipio = [row[0] for row in db.session.execute("SELECT codigo FROM esocial.municipios")]
            nome_municipio = [row[0] for row in db.session.execute("SELECT nome FROM esocial.municipios")]
            municipios = dict(zip(cod_municipio, nome_municipio))

            # Selecionando tipos logradouro
            cod_tl = [row[0] for row in db.session.execute("SELECT codigo FROM esocial.tipos_logradouro")]
            nome_tl = [row[0] for row in db.session.execute("SELECT nome FROM esocial.tipos_logradouro")]
            tipos_logradouro = dict(zip(cod_tl, nome_tl))

            # Selecionando bairros
            bairros = [row[0] for row in db.session.execute("SELECT DISTINCT nome FROM esocial.bairros")]

            return render_template("index.html", pegaso=pegaso, paises=paises, estados=estados, municipios=municipios,
                                   tl=tipos_logradouro, bairros=bairros)


if __name__ == "__main__":
    app.run(debug=True)
