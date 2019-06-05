from datetime import datetime

from flask import *
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

from _auth.views import check_login
from _form.models import *
from base import os, app

form_bp = Blueprint('form_bp', __name__)


@form_bp.route('/download_ato/<ato>/<tipo>')
def download_ato(ato, tipo):
    tipo_ato_dict = {'Nomeação': 'in', 'Exoneração': 'out'}
    tipo_ato = tipo_ato_dict[tipo]

    try:
        return send_file(os.path.join(app.static_folder, 'ato_gerado_{}.docx'.format(tipo_ato)),
                         as_attachment=True, cache_timeout=-1,
                         attachment_filename='{}_Ato_{}_{:%d%m%Y_%H%M%S}.docx'.format(ato, tipo, datetime.now()))
    except Exception as e:
        return format(e)


@form_bp.route('/upload', methods=['POST'])
def handle_upload():
    matricula = session.get('matricula')

    # Documentos - Multiple
    for key, f in request.files.items():
        if key.startswith('file'):
            if not os.path.isdir(app.config['UPLOADED_PATH']):
                os.mkdir(app.config['UPLOADED_PATH'])

            if not os.path.isdir(os.path.join(app.config['UPLOADED_PATH'], matricula)):
                os.mkdir(os.path.join(app.config['UPLOADED_PATH'], matricula))

            f.save(os.path.join(app.config['UPLOADED_PATH'], matricula, f.filename))
    return '', 204


@form_bp.route('/protected', methods=['GET', 'POST'])
def protected():
    check_login()
    matricula = session.get('matricula')

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
        # Protocolo
        # protocolo = str(matricula) + date.today().strftime('%Y%m%d')

        try:
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
        except IntegrityError:
            db.session.rollback()
            raise
        except Exception as e:
            print(format(e))

        # Dependetes
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
        return redirect(url_for('logout', cpf=cpf_trab))
    else:
        form = Trabalhador.query.filter_by(matricula=matricula)
        # Campos preenchidos através da matricula do Pegaso
        pegaso = Pegaso.query.filter_by(matr=matricula)

        if form.count() > 0:
            # Reject!
            # return redirect(url_for('logout', page='reject', protocolo=form.first().protocolo))
            return redirect(url_for('edit_worker'))
        elif pegaso.count() > 0:
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

            return render_template('index.html', pegaso=pegaso.first(), paises=paises, estados=estados,
                                   municipios=municipios, tl=tipos_logradouro, bairros=bairros)
        else:
            return render_template('401.html')


@form_bp.route('/protected/edit', methods=['GET', 'POST'])
def edit_worker():
    check_login()

    matricula = session.get('matricula')

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

        # Dependetes
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
        return redirect(url_for('logout'))

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

        return render_template('edit.html', t=trabalhador, dependentes=dependentes, paises=paises,
                               estados=estados, municipios=municipios, tl=tipos_logradouro, bairros=bairros)
    except AttributeError:
        return redirect(url_for('login'))
