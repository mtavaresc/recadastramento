from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Schema default
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/tester"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# Create all schemas
db.create_all()
