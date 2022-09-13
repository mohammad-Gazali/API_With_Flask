import os
from flask import current_app
from werkzeug.utils import secure_filename


def allowed_extention(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def get_secure_filename_filepath(file):
    filename = secure_filename(file)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    return filename, filepath