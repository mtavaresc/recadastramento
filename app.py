# -*- coding: UTF-8 -*-
from flask import render_template, request
from base import app, db
from model import Pegaso, Trabalhador

# Create all schemas
# db.create_all()


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World!"


@app.route("/<int:matricula>", methods=["GET", "POST"])
def recadastrar(matricula):
    pegaso = db.session.execute("SELECT * FROM zeus.tv_cadastro WHERE matr = '{}'".format(matricula)).first()
    print(pegaso.nome)

    if request.method == "POST":
        # Trabalhador
        cpf_trab = request.form.get("")
        nis_trab = request.form.get("")
        nm_trab = request.form.get("")
        sexo = request.form.get("")
        raca_cor = request.form.get("")
        est_civ = request.form.get("")
        grau_instr = request.form.get("")
        ind_pri_empr = request.form.get("")
        nm_soc = request.form.get("")
        # Nascimento
        dt_nascto = request.form.get("")
        cod_munic = request.form.get("")
        uf = request.form.get("")
        pais_nascto = request.form.get("")
        pais_nac = request.form.get("")
        nm_mae = request.form.get("")
        nm_pai = request.form.get("")
        # CTPS
        nr_ctps = request.form.get("")
        serie_ctps = request.form.get("")
        uf_ctps = request.form.get("")
        # RIC
        # nr_ric = request.form.get("")
        # ric_orgao_emissor = request.form.get("")
        # ric_dt_exped = request.form.get("")
        # RG
        nr_rg = request.form.get("")
        rg_orgao_emissor = request.form.get("")
        rg_dt_exped = request.form.get("")
        # RNE
        # nr_rne = request.form.get("")
        # rne_orgao_emissor = request.form.get("")
        # rne_dt_exped = request.form.get("")
        # OC
        nr_oc = request.form.get("")
        oc_orgao_emissor = request.form.get("")
        oc_dt_exped = request.form.get("")
        oc_dt_valid = request.form.get("")
        # CNH
        nr_reg_cnh = request.form.get("")
        cnh_dt_exped = request.form.get("")
        uf_cnh = request.form.get("")
        cnh_dt_valid = request.form.get("")
        dt_pri_hab = request.form.get("")
        categoria_cnh = request.form.get("")
        # Endereco - Brasil
        tp_lograd = request.form.get("")
        dsc_lograd = request.form.get("")
        nr_lograd = request.form.get("")
        complemento = request.form.get("")
        bairro = request.form.get("")
        cep = request.form.get("")
        end_cod_munic = request.form.get("")
        end_uf = request.form.get("")
        # Endereco - Exterior
        pais_resid = request.form.get("")
        ext_dsc_lograd = request.form.get("")
        ext_nr_lograd = request.form.get("")
        ext_complemento = request.form.get("")
        ext_bairro = request.form.get("")
        nm_cid = request.form.get("")
        cod_postal = request.form.get("")
        # Estrangeiro
        # dt_chegada = request.form.get("")
        # class_trab_estran = request.form.get("")
        # casado_br = request.form.get("")
        # filhos_br = request.form.get("")
        # Info Deficiencia
        def_fisica = request.form.get("")
        def_visual = request.form.get("")
        def_auditiva = request.form.get("")
        def_mental = request.form.get("")
        def_intelectual = request.form.get("")
        def_readap = request.form.get("")
        info_cota = request.form.get("")
        observacao = request.form.get("")
        # Dependete
        tp_dep = request.form.get("")
        nm_dep = request.form.get("")
        dep_dt_nascto = request.form.get("")
        cpf_dep = request.form.get("")
        dep_irrf = request.form.get("")
        dep_sf = request.form.get("")
        inc_trab = request.form.get("")
        # Aposentadoria
        trab_aposent = request.form.get("")
        # Contato
        fone_princ = request.form.get("")
        fone_alternat = request.form.get("")
        email_princ = request.form.get("")
        email_alternat = request.form.get("")

        c = Trabalhador(cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr, nm_soc,
                        dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, nm_pai, nr_ctps, serie_ctps, uf_ctps,
                        nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor, oc_dt_exped, oc_dt_valid,
                        nr_reg_cnh, cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab, categoria_cnh, tp_lograd,
                        dsc_lograd, nr_lograd, complemento, bairro, cep, end_cod_munic, end_uf, pais_resid,
                        ext_dsc_lograd, ext_nr_lograd, ext_complemento, ext_bairro, nm_cid, cod_postal, def_fisica,
                        def_visual, def_auditiva, def_mental, def_intelectual, def_readap, info_cota, observacao,
                        tp_dep, nm_dep, dep_dt_nascto, cpf_dep, dep_irrf, dep_sf, inc_trab, trab_aposent, fone_princ,
                        fone_alternat, email_princ, email_alternat)
        db.session.merge(c)
        db.session.commit()

        return render_template("submit.html")

    return render_template("index.html", pegaso=pegaso)


if __name__ == "__main__":
    app.run(debug=True)
