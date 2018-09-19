from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///alece.db"
SQLALCHEMY_BINDS = {
    "in": SQLALCHEMY_DATABASE_URI,  # pegaso
    "out": SQLALCHEMY_DATABASE_URI  # trabalhador
}

app = Flask(__name__)
db = SQLAlchemy(app)
