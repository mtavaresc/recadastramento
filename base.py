from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

url = "oracle+cx_oracle://esocial:teste1423@10.85.100.59:1521/PROD"
# Schema default
app.config["SQLALCHEMY_DATABASE_URI"] = url
# Schema additional
# app.config["SQLALCHEMY_BINDS"] = {
#     "new_db": "oracle+cx_oracle://esocial:teste1423@10.85.100.59:1521/PROD"
# }

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# Create all schemas
db.create_all()
