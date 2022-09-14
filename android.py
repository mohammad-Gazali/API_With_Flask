from flask import Blueprint, request, jsonify, redirect, url_for, current_app
from helpers import get_secure_filename_filepath
from PIL import Image
from zipfile import ZipFile
from datetime import datetime
import os
import shutil

bp = Blueprint('android', __name__, url_prefix='/android')


ICON_SIZES = [29, 40, 57, 58, 60, 80, 87, 114, 120, 180, 1024]


@bp.route('/', methods=['POST'])
def create_images():
    file = request.json['filename']
    filename, filepath = get_secure_filename_filepath(file)

    tempfolder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'temp')
    os.makedirs(tempfolder)

    try:
        for size in ICON_SIZES:
            outfile = os.path.join(tempfolder, f'{size}.png')
            image = Image.open(filepath)
            out = image.resize((size, size))
            out.save(outfile, 'PNG')
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404

    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).split('.')[0]

    zipfilename = f'{timestamp}.zip'
    zipfilepath = os.path.join(current_app.config['UPLOAD_FOLDER'], zipfilename)

    with ZipFile(zipfilepath, 'w') as zip_obj:
        for foldername, subfolders, filenames in os.walk(tempfolder):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zip_obj.write(filepath, os.path.basename(filepath))
        shutil.rmtree(tempfolder)
        return redirect(url_for('download_file', name=zipfilename))