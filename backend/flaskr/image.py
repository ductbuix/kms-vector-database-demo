import os
from flask import ( Blueprint, request, jsonify, send_file )
from werkzeug.utils import secure_filename

from flaskr.utils.search_image import p_search_pre_yolo
from flaskr import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, IMAGE_RESULT_FOLDER
from towhee import DataCollection

bp = Blueprint('image', __name__, url_prefix='/images')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('', methods=['POST'])
def search():
    if 'file' not in request.files:
        return jsonify({ "message": "Please Input File in Form Data" }), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({ "message": "Filename cannot be blank"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename((file.filename))
        image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), UPLOAD_FOLDER, filename)
        file.save(image_path)
        res = p_search_pre_yolo(image_path)
        result = []
        for r in  DataCollection(res).to_list():
            result.extend(r.pred)
        return { "result":  result }
    else:
        jsonify({ "message": "File is not allowed"}), 400


@bp.route('/<path:subpath>', methods=['GET'])
def get(subpath):
    try:
        image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), IMAGE_RESULT_FOLDER, subpath)
        response = send_file(image_path)
        return response
    except FileNotFoundError:
        return jsonify({ "message":  "File not found" })
