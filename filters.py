from flask import Blueprint, request, url_for, redirect, jsonify
from helpers import get_secure_filename_filepath
from PIL import Image, ImageFilter, ImageEnhance

bp = Blueprint('filters', __name__, url_prefix='/filters')


@bp.route('/blur', methods=['POST'])
def blur():
    file = request.json['filename']
    filename, filepath = get_secure_filename_filepath(file)

    try:
        radius = int(request.json['radius'])
        image = Image.open(filepath)
        out = image.filter(ImageFilter.GaussianBlur(radius))
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404


@bp.route('/contrast', methods=['POST'])
def contrast():
    file = request.json['filename']
    filename, filepath = get_secure_filename_filepath(file)

    try:
        factor = float(request.json['factor'])
        image = Image.open(filepath)
        out = ImageEnhance.Contrast(image).enhance(factor)
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404


@bp.route('/brightness', methods=['POST'])
def brightness():
    file = request.json['filename']
    filename, filepath = get_secure_filename_filepath(file)

    try:
        factor = float(request.json['factor'])
        image = Image.open(filepath)
        out = ImageEnhance.Brightness(image).enhance(factor)
        out.save(filepath)
        return redirect(url_for('download_file', name=filename))
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404