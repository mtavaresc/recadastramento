# -*- coding: utf-8 -*-
from datetime import datetime, date

import requests
from flask import *
from mailmerge import MailMerge
from sqlalchemy import func, and_
from sqlalchemy.exc import IntegrityError

from _admin.models import *
from _form.models import *
from _auth.views import check_login
from _auth.models import User
from base import os, basedir

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/admin')
def admin():
    check_login()

    adm = db.session.query(User.nome, Trabalhador.protocolo, Trabalhador.sexo). \
        outerjoin(Trabalhador, User.matricula == Trabalhador.matricula). \
        filter(User.matricula == session.get('matricula')).first()

    # Pendente
    p = db.session.query(Pegaso).filter(Pegaso.matr.notin_(db.session.query(Trabalhador.matricula))).count()
    # Em análise
    ea = db.session.query(Trabalhador).filter(Trabalhador.protocolo.is_(None)).count()
    # Realizado
    r = db.session.query(Trabalhador).filter(Trabalhador.protocolo.isnot(None)).count()

    return render_template('admin/dashboard.html', adm=adm, pendente=p, realizado=r, em_analise=ea)


@admin_bp.route('/admin/controle-cadastro', methods=['GET', 'POST'])
def admin_controle_cadastro():
    check_login()

    if request.method == 'POST':
        try:
            protocolo = request.form.get('protocol')
            matr = protocolo[:6]

            Trabalhador.query.filter_by(matricula=matr).update({'protocolo': protocolo})
            db.session.commit()
        except Exception as e:
            return '#1: {}'.format(e)

        try:
            a = Auditoria(matradm=session.get('matricula'), matricula=matr, action='Validar', created=datetime.now())
            db.session.add(a)
            db.session.commit()
        except Exception as e:
            return '#2: {}'.format(e)

    adm = db.session.query(User.nome, Trabalhador.protocolo, Trabalhador.sexo). \
        outerjoin(Trabalhador, User.matricula == Trabalhador.matricula). \
        filter(User.matricula == session.get('matricula')).first()

    w = Trabalhador.query

    return render_template('admin/controle/cadastro.html', adm=adm, data=w, date=date.today().strftime('%Y%m%d'))


@admin_bp.route('/admin/controle-lotacao/<indice>', defaults={'competencia': 'False', 'sit': 1},
                methods=['GET', 'POST'])
@admin_bp.route('/admin/controle-lotacao/<indice>/<sit>/<competencia>', methods=['GET', 'POST'])
def admin_controle_lotacao(indice, competencia, sit):
    check_login()

    if request.method == 'POST':
        ato = request.form.get('ato')
        if ato is not None:
            data_ato = request.form.get('data')
            carfun = request.form.get('carfun')
            lot = request.form.get('lot')
            tipo_ato = request.form.get('tipo_ato')

            tipo_ato_dict = {'in': 'Nomeação', 'out': 'Exoneração'}

            if competencia != 'False' and len(competencia) == 8:
                url = '{host}admin/controle-lotacao/detalhe/{car}+{lot}+{sit}+{comp}'.format(host=request.host_url,
                                                                                             car=carfun, lot=lot,
                                                                                             sit=sit, comp=competencia)
            else:
                url = '{host}admin/controle-lotacao/detalhe/{car}+{lot}+{sit}'.format(host=request.host_url, car=carfun,
                                                                                      lot=lot, sit=sit)
            requests.post(url, data={'ato': ato, 'data': data_ato, 'tipo_ato': tipo_ato})

            flash('Ato {} de {} criado com sucesso!'.format(ato.replace('/', ''), tipo_ato_dict[tipo_ato]), 'success')
            return redirect(url_for('admin'))
        else:
            mes = request.form.get('mes')
            ano = request.form.get('ano')
            fin_sit = request.form.get('fin_sit')
            competencia = '01{mes}{ano}'.format(mes=mes, ano=ano)

            return redirect(url_for('admin_controle_lotacao', indice=indice, sit=fin_sit, competencia=competencia))

    adm = db.session.query(User.nome, Trabalhador.protocolo, Trabalhador.sexo). \
        outerjoin(Trabalhador, User.matricula == Trabalhador.matricula). \
        filter(User.matricula == session.get('matricula')).first()

    if int(sit) == 1:
        hst = 'S'
    else:
        hst = 'N'

    if indice == 'gt':
        if competencia != 'False' and len(competencia) == 8:
            consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                        func.count(Cadastro.cad_matr).label('qtd_matr')) \
                .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
                .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
                .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
                .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
                .filter(
                and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
                     Lotacao.lot_desc.like('{}%'.format(indice.upper())),
                     Lotacao.lot_cod.like('GT38%'),
                     Financeiro.fin_folha == '03',
                     CargoFuncao.car_ativo == 'S',
                     HistoricoFuncao.hst == hst,
                     Financeiro.fin_sit == int(sit),
                     func.extract('month', HistoricoFuncao.hdtini) == int(competencia[2:4]),
                     func.extract('year', HistoricoFuncao.hdtini) == int(competencia[4:8]))) \
                .group_by(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc) \
                .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)
        else:
            consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                        func.count(Cadastro.cad_matr).label('qtd_matr')) \
                .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
                .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
                .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
                .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
                .filter(
                and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
                     Lotacao.lot_desc.like('{}%'.format(indice.upper())),
                     Lotacao.lot_cod.like('GT38%'),
                     Financeiro.fin_folha == '03',
                     CargoFuncao.car_ativo == 'S',
                     Financeiro.fin_sit == int(sit),
                     HistoricoFuncao.hst == hst)) \
                .group_by(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc) \
                .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)
    else:
        if competencia != 'False' and len(competencia) == 8:
            consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                        func.count(Cadastro.cad_matr).label('qtd_matr')) \
                .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
                .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
                .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
                .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
                .filter(
                and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
                     Lotacao.lot_desc.like('{}%'.format(indice.upper())),
                     Financeiro.fin_folha == '03',
                     CargoFuncao.car_ativo == 'S',
                     HistoricoFuncao.hst == hst,
                     Financeiro.fin_sit == int(sit),
                     func.extract('month', HistoricoFuncao.hdtini) == int(competencia[2:4]),
                     func.extract('year', HistoricoFuncao.hdtini) == int(competencia[4:8]))) \
                .group_by(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc) \
                .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)
        else:
            consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                        func.count(Cadastro.cad_matr).label('qtd_matr')) \
                .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
                .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
                .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
                .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
                .filter(
                and_(CargoFuncao.car_cod.in_(['G001', 'G002', 'G004', 'G005', 'G006']),
                     Lotacao.lot_desc.like('{}%'.format(indice.upper())),
                     Financeiro.fin_folha == '03',
                     CargoFuncao.car_ativo == 'S',
                     Financeiro.fin_sit == int(sit),
                     HistoricoFuncao.hst == hst)) \
                .group_by(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc) \
                .order_by(CargoFuncao.car_desc, Lotacao.lot_desc)

    return render_template('admin/controle/lotacao.html', adm=adm, data=consulta, indice=indice)


@admin_bp.route('/admin/controle-lotacao/detalhe/<carfun>+<lot>+<sit>', defaults={'competencia': 'False'},
                methods=['GET', 'POST'])
@admin_bp.route('/admin/controle-lotacao/detalhe/<carfun>+<lot>+<sit>+<competencia>', methods=['GET', 'POST'])
def admin_controle_lotacao_detalhe(carfun, lot, competencia, sit):
    ff2 = db.session.query(FichaFinanceira.fic_matr, func.max(FichaFinanceira.fic_codfp).label('ultima')) \
        .group_by(FichaFinanceira.fic_matr).subquery()

    ff1 = db.session.query(FichaFinanceira.fic_matr, FichaFinanceira.fic_valor) \
        .join(ff2, and_(ff2.c.fic_matr == FichaFinanceira.fic_matr, ff2.c.ultima == FichaFinanceira.fic_codfp)) \
        .filter(FichaFinanceira.fic_cod.in_(['109', '139'])).subquery()

    if int(sit) == 1:
        hst = 'S'
    else:
        hst = 'N'

    if competencia != 'False' and len(competencia) == 8:
        consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                    Lotacao.lot_desctot, Lotacao.lot_ato, Lotacao.lot_dtato, Cadastro.cad_matr,
                                    Cadastro.cad_nome, ff1.c.fic_valor) \
            .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
            .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
            .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
            .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
            .join(ff1, ff1.c.fic_matr == Cadastro.cad_matr) \
            .filter(
            and_(CargoFuncao.car_cod == carfun,
                 Lotacao.lot_cod == lot,
                 Financeiro.fin_folha == '03',
                 CargoFuncao.car_ativo == 'S',
                 HistoricoFuncao.hst == hst,
                 Financeiro.fin_sit == int(sit),
                 func.extract('month', HistoricoFuncao.hdtini) == int(competencia[2:4]),
                 func.extract('year', HistoricoFuncao.hdtini) == int(competencia[4:8]))) \
            .order_by(Cadastro.cad_nome)
    else:
        consulta = db.session.query(CargoFuncao.car_cod, CargoFuncao.car_desc, Lotacao.lot_cod, Lotacao.lot_desc,
                                    Lotacao.lot_desctot, Lotacao.lot_ato, Lotacao.lot_dtato, Cadastro.cad_matr,
                                    Cadastro.cad_nome, ff1.c.fic_valor) \
            .join(HistoricoFuncao, CargoFuncao.car_cod == HistoricoFuncao.hcodcarfun) \
            .join(Cadastro, Cadastro.cad_matr == HistoricoFuncao.hmatr) \
            .join(Lotacao, Lotacao.lot_cod == Cadastro.cad_lotori) \
            .join(Financeiro, Cadastro.cad_matr == Financeiro.fin_matr) \
            .join(ff1, ff1.c.fic_matr == Cadastro.cad_matr) \
            .filter(
            and_(CargoFuncao.car_cod == carfun,
                 Lotacao.lot_cod == lot,
                 Financeiro.fin_folha == '03',
                 CargoFuncao.car_ativo == 'S',
                 Financeiro.fin_sit == int(sit),
                 HistoricoFuncao.hst == hst)) \
            .order_by(Cadastro.cad_nome)

    if request.method == 'POST':
        ato = request.form.get('ato')
        data_ato = datetime.strptime(request.form.get('data'), '%Y-%m-%d')
        tipo_ato = request.form.get('tipo_ato')

        template = os.path.join(basedir, 'static', 'ato_{}.docx'.format(tipo_ato))

        full_months = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
                       5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
                       9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

        hoje = date.today()

        input_data_1 = '{dia} de {mes} de {ano}'.format(dia=data_ato.day, mes=full_months[data_ato.month],
                                                        ano=data_ato.year)
        input_data_2 = '{dia} dias do mês de {mes} de {ano}'.format(dia=hoje.day, mes=full_months[hoje.month],
                                                                    ano=hoje.year)
        dtato = consulta.first().lot_dtato
        lot_dtato = '{dia} de {mes} de {ano}'.format(dia=dtato.day, mes=full_months[dtato.month], ano=dtato.year)

        document = MailMerge(template)

        if tipo_ato == 'in':
            document.merge(
                Ato=ato,
                lot_ato=consulta.first().lot_ato,
                lot_desctot=consulta.first().lot_desctot,
                input_data_1=input_data_1,
                input_data_2=input_data_2
            )
        else:
            document.merge(
                Ato=ato,
                lot_ato=consulta.first().lot_ato,
                lot_desctot=consulta.first().lot_desctot,
                lot_dtato=lot_dtato,
                input_data_1=input_data_1,
                input_data_2=input_data_2
            )

        funcionarios = []
        car_desc = consulta.first().car_desc
        for row in consulta:
            funcionarios.append({'car_desc': car_desc, 'nome': row.cad_nome})

        document.merge_rows('car_desc', funcionarios)

        f = 'ato_gerado_{}.docx'.format(tipo_ato)
        document.write(os.path.join(basedir, 'static', f))

    return render_template('admin/controle/detalhe.html', data=consulta, carfun=carfun, lot=lot,
                           desc=consulta.first().lot_desc)


@admin_bp.route('/admin/worker/<matricula>', methods=['GET', 'POST'])
def admin_edit_worker(matricula):
    check_login()

    if request.method == 'POST':
        # Trabalhador
        cpf_trab = request.form.get('cpfTrab')
        cpf_trab = ''.join(c for c in str(cpf_trab) if c not in '.-')
        nis_trab = request.form.get('nisTrab')
        nis_trab = ''.join(c for c in str(nis_trab) if c not in '.-')
        nm_trab = request.form.get('nmTrab')
        sexo = request.form.get('sexo')
        raca_cor = request.form.get('racaCor')
        est_civ = request.form.get('estCiv')
        grau_instr = request.form.get('grauInstr')
        ind_pri_empr = request.form.get('indPriEmpr')
        nm_soc = request.form.get('nmSoc')
        # Nascimento
        dt_nascto = func.to_date(request.form.get('dtNascto'), 'YYYY-MM-DD')
        cod_munic = request.form.get('codMunic')
        uf = request.form.get('uf')
        pais_nascto = request.form.get('paisNascto')
        pais_nac = request.form.get('paisNac')
        nm_mae = request.form.get('nmMae')
        cpf_mae = request.form.get('cpfMae')
        cpf_mae = ''.join(c for c in str(cpf_mae) if c not in '.-')
        nm_pai = request.form.get('nmPai')
        cpf_pai = request.form.get('cpfPai')
        cpf_pai = ''.join(c for c in str(cpf_pai) if c not in '.-')
        # CTPS
        nr_ctps = request.form.get('nrCtps')
        serie_ctps = request.form.get('serieCtps')
        uf_ctps = request.form.get('ufCtps')
        # RG
        nr_rg = request.form.get('nrRg')
        rg_orgao_emissor = request.form.get('rg_orgaoEmissor')
        rg_dt_exped = func.to_date(request.form.get('rg_dtExped'), 'YYYY-MM-DD')
        # OC
        nr_oc = request.form.get('nrOc')
        oc_orgao_emissor = request.form.get('oc_orgaoEmissor')
        oc_dt_exped = None if request.form.get('oc_dtExped') is '' else func.to_date(request.form.get('oc_dtExped'),
                                                                                     'YYYY-MM-DD')
        oc_dt_valid = None if request.form.get('oc_dtValid') is '' else func.to_date(request.form.get('oc_dtValid'),
                                                                                     'YYYY-MM-DD')
        # CNH
        nr_reg_cnh = request.form.get('nrRegCnh')
        cnh_dt_exped = None if request.form.get('cnh_dtExped') is '' else func.to_date(request.form.get('cnh_dtExped'),
                                                                                       'YYYY-MM-DD')
        uf_cnh = request.form.get('ufCnh')
        cnh_dt_valid = None if request.form.get('cnh_dtValid') is '' else func.to_date(request.form.get('cnh_dtValid'),
                                                                                       'YYYY-MM-DD')
        dt_pri_hab = None if request.form.get('dtPriHab') is '' else func.to_date(request.form.get('dtPriHab'),
                                                                                  'YYYY-MM-DD')
        categoria_cnh = request.form.get('categoriaCnh')
        # Endereco - Brasil
        tp_lograd = request.form.get('tpLograd')
        dsc_lograd = request.form.get('dscLograd')
        nr_lograd = request.form.get('nrLograd')
        complemento = request.form.get('complemento')
        bairro = request.form.get('bairro')
        cep = request.form.get('cep')
        cep = ''.join(c for c in str(cep) if c not in '-')
        end_cod_munic = request.form.get('end_codMunic')
        end_uf = request.form.get('end_uf')
        # Info Deficiencia
        def_fisica = request.form.get('defFisica')
        def_visual = request.form.get('defVisual')
        def_auditiva = request.form.get('defAuditiva')
        def_mental = request.form.get('defMental')
        def_intelectual = request.form.get('defIntelectual')
        def_readap = request.form.get('defReadap')
        info_cota = request.form.get('infoCota')
        observacao = request.form.get('observacao')
        # Aposentadoria
        trab_aposent = request.form.get('trabAposent')
        # Contatos
        fone_princ = request.form.get('fonePrinc')
        fone_princ = ''.join(c for c in str(fone_princ) if c not in '()- ')
        fone_alternat = request.form.get('foneAlternat')
        fone_alternat = ''.join(c for c in str(fone_alternat) if c not in '()- ')
        email_princ = request.form.get('emailPrinc')
        email_alternat = request.form.get('emailAlternat')

        c = Trabalhador(matricula, cpf_trab, nis_trab, nm_trab, sexo, raca_cor, est_civ, grau_instr, ind_pri_empr,
                        nm_soc, dt_nascto, cod_munic, uf, pais_nascto, pais_nac, nm_mae, cpf_mae, nm_pai, cpf_pai,
                        nr_ctps, serie_ctps, uf_ctps, nr_rg, rg_orgao_emissor, rg_dt_exped, nr_oc, oc_orgao_emissor,
                        oc_dt_exped, oc_dt_valid, nr_reg_cnh, cnh_dt_exped, uf_cnh, cnh_dt_valid, dt_pri_hab,
                        categoria_cnh, tp_lograd, dsc_lograd, nr_lograd, complemento, bairro, cep, end_cod_munic,
                        end_uf, def_fisica, def_visual, def_auditiva, def_mental, def_intelectual, def_readap,
                        info_cota, observacao, trab_aposent, fone_princ, fone_alternat, email_princ, email_alternat,
                        None)

        db.session.merge(c)
        db.session.commit()

        # Dependentes
        tp_dep = request.form.getlist('tpDep[]')
        nm_dep = request.form.getlist('nmDep[]')
        dep_dt_nascto = request.form.getlist('dep_dtNascto[]')
        cpf_dep = request.form.getlist('cpfDep[]')
        dep_irrf = request.form.getlist('depIRRF[]')
        dep_sf = request.form.getlist('depSF[]')
        inc_trab = request.form.getlist('incTrab[]')

        try:
            for i in range(len(tp_dep)):
                dtnascimento = func.to_date(dep_dt_nascto[i], 'YYYY-MM-DD')
                cpf = ''.join(c for c in str(cpf_dep[i]) if c not in '.-')

                if cpf is not None and cpf != '':
                    d = Dependentes(matricula, tp_dep[i], nm_dep[i], dtnascimento, cpf, dep_irrf[i], dep_sf[i],
                                    inc_trab[i])
                    db.session.merge(d)
                    db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise

        # Logout!
        try:
            a = Auditoria(session.get('matricula'), matricula, 'Editar', datetime.now())
            db.session.add(a)
            db.session.commit()
        except Exception as e:
            return '#Auditoria: {}'.format(e)

        return redirect(url_for('admin'))

    try:
        trabalhador = Trabalhador.query.filter_by(matricula=matricula).first()
        dependentes = Dependentes.query.filter_by(matrtab=trabalhador.matricula).all()

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

        return render_template('admin/edit.html', t=trabalhador, dependentes=dependentes, paises=paises,
                               estados=estados, municipios=municipios, tl=tipos_logradouro, bairros=bairros)
    except AttributeError:
        return redirect(url_for('login'))
