from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///alece.db"
SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://dionisio:baco@10.85.100.59:1521/prod"
SQLALCHEMY_BINDS = {
    "get": SQLALCHEMY_DATABASE_URI,  # pegaso
    "set": SQLALCHEMY_DATABASE_URI  # trabalhador
}

app = Flask(__name__)
db = SQLAlchemy(app)
