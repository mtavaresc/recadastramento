import os
from datetime import timedelta

from flask import Flask
from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.WE8ISO8859P1'

app = Flask(__name__)
app.secret_key = b'~\xde\xba\xc6\x16"O.\x0e\x95\xbet\xdfbZ\x03'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3000)

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{tnsname}/{sid}'.format(
    username='esocial',
    password='teste1423',
    tnsname='10.85.100.59',
    # tnsname='localhost',
    sid='PROD'
    # sid='XE'
)

# SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_NATIVE_UNICODE'] = 'ISO-8859-1'

# Dropzone settings
dropzone = Dropzone(app)
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'docs')
app.config['DROPZONE_IN_FORM'] = True
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf'
app.config['DROPZONE_UPLOAD_ON_CLICK'] = True
app.config['DROPZONE_UPLOAD_ACTION'] = 'handle_upload'
app.config['DROPZONE_UPLOAD_BTN_ID'] = 'enviar'
app.config['DROPZONE_DEFAULT_MESSAGE'] = 'Arraste os documentos aqui ou clique para procurar'

db = SQLAlchemy(app)
