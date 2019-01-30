import os
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8ISO8859P1"

app = Flask(__name__)
app.secret_key = b'~\xde\xba\xc6\x16"O.\x0e\x95\xbet\xdfbZ\x03'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3000)

url = "oracle+cx_oracle://esocial:teste1423@10.85.100.59:1521/PROD"
# url = "oracle+cx_oracle://esocial:teste1423@localhost:1521/XE"

# SQLAlchemy settings
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_NATIVE_UNICODE"] = "ISO-8859-1"

# Dropzone settings
dropzone = Dropzone(app)
app.config["DROPZONE_UPLOAD_MULTIPLE"] = True
app.config["DROPZONE_ALLOWED_FILE_CUSTOM"] = True
app.config["DROPZONE_ALLOWED_FILE_TYPE"] = 'image/*'
app.config["DROPZONE_REDIRECT_VIEW"] = 'sandbox_results'

# Uploads settings
app.config["UPLOADED_PHOTOS_DEST"] = os.path.join(os.getcwd(), 'uploads')

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
