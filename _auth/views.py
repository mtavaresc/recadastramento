# -*- coding: utf-8 -*-
from datetime import datetime

from flask import *

from _auth.models import *

auth_bp = Blueprint('auth_bp', __name__)


def check_login():
    if session.get('logged_in') is None or session.get('matricula') is None:
        return render_template('login.html')


@auth_bp.errorhandler(404)
def page_not_found(e):
    session.clear()
    return render_template('404.html'), 404


@auth_bp.errorhandler(401)
def unauthorized_access(e):
    session.clear()
    return render_template('401.html'), 401


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            session.clear()
            return render_template('login.html')
        elif request.method == 'POST':
            data = User.query.filter_by(matricula=request.form.get('matricula'),
                                        senha=request.form.get('senha')).first()
            if data is not None:
                session['logged_in'] = True
                session['matricula'] = data.matricula
                if data.adm == 1:
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('protected'))
            else:
                return render_template('noauth.html')
    except AttributeError:
        return render_template('401.html')


@auth_bp.route('/logout/<cpf>')
def logout(cpf):
    session.clear()
    return render_template('submit.html', cpf=cpf, agora=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
