from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os

os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8ISO8859P1"

app = Flask(__name__)
app.secret_key = b'~\xde\xba\xc6\x16"O.\x0e\x95\xbet\xdfbZ\x03'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3000)

url = "oracle+cx_oracle://esocial:teste1423@10.85.100.59:1521/PROD"
# url = "oracle+cx_oracle://esocial:teste1423@localhost:1521/XE"

# Schema default
app.config["SQLALCHEMY_DATABASE_URI"] = url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_NATIVE_UNICODE"] = "ISO-8859-1"

db = SQLAlchemy(app)
