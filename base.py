from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Schema default
app.config["SQLALCHEMY_DATABASE_URI"] = "oracle+cx_oracle://dionisio:baco@10.85.100.59/prod"
# Schema additional
app.config["SQLALCHEMY_BINDS"] = {
    "new_db": "oracle+cx_oracle://dionisio:baco@10.85.100.59/prod"
}

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# Create all schemas
db.create_all()
