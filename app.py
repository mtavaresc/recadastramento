# -*- coding: utf-8 -*-
# Native
from datetime import date
# External
from flask import render_template, request, redirect, url_for, session, escape
from sqlalchemy import func
# Owner
from base import app
from model import *


@app.errorhandler(404)
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")

        cauth = User.query.filter_by(matricula=matricula, senha=senha).count()
        form = Trabalhador.query.filter_by(matricula=matricula)

        if cauth > 0:
            if form.count() > 0:
                return render_template("reject.html", protocolo=form.first().protocolo)
            else:
                session['matricula'] = matricula
                return redirect(url_for("recadastrar"))
        else:
            return render_template("noauth.html")

    return render_template("login.html")


@app.route("/protected", methods=["GET", "POST"])
def recadastrar():
    if 'matricula' in session:
        matricula = escape(session['matricula'])
        session.pop('matricula', None)

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
            dt_nascto = func.to_date(request.form.get("dtNascto"), 'YYYY-MM-DD')
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
            rg_dt_exped = func.to_date(request.form.get("rg_dtExped"), 'YYYY-MM-DD')
            # OC
            nr_oc = request.form.get("nrOc")
            oc_orgao_emissor = request.form.get("oc_orgaoEmissor")
            oc_dt_exped = None if request.form.get("oc_dtExped") is "" else func.to_date(request.form.get("oc_dtExped"), 'YYYY-MM-DD')
            oc_dt_valid = None if request.form.get("oc_dtValid") is "" else func.to_date(request.form.get("oc_dtValid"), 'YYYY-MM-DD')
            # CNH
            nr_reg_cnh = request.form.get("nrRegCnh")
            cnh_dt_exped = None if request.form.get("cnh_dtExped") is "" else func.to_date(request.form.get("cnh_dtExped"), 'YYYY-MM-DD')
            uf_cnh = request.form.get("ufCnh")
            cnh_dt_valid = None if request.form.get("cnh_dtValid") is "" else func.to_date(request.form.get("cnh_dtValid"), 'YYYY-MM-DD')
            dt_pri_hab = None if request.form.get("dtPriHab") is "" else func.to_date(request.form.get("dtPriHab"), 'YYYY-MM-DD')
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
            # Info Deficiencia
            def_fisica = request.form.get("defFisica")
            def_visual = request.form.get("defVisual")
            def_auditiva = request.form.get("defAuditiva")
            def_mental = request.form.get("defMental")
            def_intelectual = request.form.get("defIntelectual")
            def_readap = request.form.get("defReadap")
            info_cota = request.form.get("infoCota")
            observacao = request.form.get("observacao")
            # Dependetes
            qtd_dep = request.form.get("qtdDep")
            # Aposentadoria
            trab_aposent = request.form.get("trabAposent")
            # Contatos
            fone_princ = request.form.get("fonePrinc")
            fone_princ = "".join(c for c in str(fone_princ) if c not in "()- ")
            fone_alternat = request.form.get("foneAlternat")
            fone_alternat = "".join(c for c in str(fone_alternat) if c not in "()- ")
            email_princ = request.form.get("emailPrinc")
            email_alternat = request.form.get("emailAlternat")
            # Protocolo
            protocolo = matricula + date.today().strftime("%Y%m%d")

            c = Trabalhador(matricula, cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr,
                            nm_soc, dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, nm_pai, nr_ctps, serie_ctps,
                            uf_ctps, nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor, oc_dt_exped,
                            oc_dt_valid, nr_reg_cnh, cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab, categoria_cnh,
                            tp_lograd, dsc_lograd, nr_lograd, complemento, bairro, cep, end_cod_munic, end_uf, def_fisica,
                            def_visual, def_auditiva, def_mental, def_intelectual, def_readap, info_cota, observacao,
                            qtd_dep, trab_aposent, fone_princ, fone_alternat, email_princ, email_alternat, protocolo)
            db.session.merge(c)
            db.session.commit()

            # Dependetes
            tp_dep = request.form.getlist("tpDep[]")
            nm_dep = request.form.getlist("nmDep[]")
            dep_dt_nascto = request.form.getlist("dep_dtNascto[]")
            cpf_dep = request.form.getlist("cpfDep[]")
            dep_irrf = request.form.getlist("depIRRF[]")
            dep_sf = request.form.getlist("depSF[]")
            inc_trab = request.form.getlist("incTrab[]")

            for i in range(len(tp_dep)):
                dtnascimento = func.to_date(dep_dt_nascto[i], 'YYYY-MM-DD')
                cpf = "".join(c for c in str(cpf_dep[i]) if c not in ".-")

                d = Dependentes(matricula, tp_dep[i], nm_dep[i], dtnascimento, cpf, dep_irrf[i], dep_sf[i], inc_trab[i])
                db.session.merge(d)
                db.session.commit()

            return render_template("submit.html", protocolo=protocolo)
        else:
            form = Trabalhador.query.filter_by(matricula=matricula)

            if form.count() > 0:
                return render_template("reject.html", protocolo=form.first().protocolo)
            else:
                # Campos preenchidos através da matricula do Pegaso
                pegaso = Pegaso.query.filter_by(matricula=matricula)

                if pegaso.count() > 0:
                    # Selecionando paises
                    cod_paises = [row.codigo for row in Paises.query.all()]
                    nome_paises = [row.nome for row in Paises.query.all()]
                    paises = dict(zip(cod_paises, nome_paises))
                    # Selecionando estados
                    uf_estados = [row.uf for row in Estados.query.all()]
                    nome_estados = [row.nome for row in Estados.query.all()]
                    estados = dict(zip(uf_estados, nome_estados))
                    # Selecionando municipios
                    cod_municipio = [row.codigo for row in Municipios.query.all()]
                    nome_municipio = [row.nome for row in Municipios.query.all()]
                    municipios = dict(zip(cod_municipio, nome_municipio))
                    # Selecionando tipos logradouro
                    cod_tl = [row.codigo for row in TiposLogradouro.query.all()]
                    nome_tl = [row.nome for row in TiposLogradouro.query.all()]
                    tipos_logradouro = dict(zip(cod_tl, nome_tl))
                    # Selecionando bairros
                    bairros = [row.nome for row in db.session.query(Bairros.nome).distinct().order_by(Bairros.nome).all()]

                    return render_template("index.html", pegaso=pegaso.first(), paises=paises, estados=estados,
                                           municipios=municipios, tl=tipos_logradouro, bairros=bairros)
                else:
                    return render_template("noauth.html")
    else:
        return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
