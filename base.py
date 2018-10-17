from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# url = "oracle+cx_oracle://esocial:teste1423@10.85.100.59:1521/PROD"
url = "oracle+cx_oracle://esocial:teste1423@localhost:1521/XE"

# Schema default
app.config["SQLALCHEMY_DATABASE_URI"] = url

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_NATIVE_UNICODE"] = "ISO-8859-1"

db = SQLAlchemy(app)
