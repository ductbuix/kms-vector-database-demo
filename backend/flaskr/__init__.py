from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = 'images'
PDF_UPLOAD_FOLDER = 'files'
TXT_UPLOAD_FOLDER = 'files'
IMAGE_RESULT_FOLDER = 'utils'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'txt'}
PDF_ALLOWED_EXTENSIONS = {'pdf'}
TXT_ALLOWED_EXTENSIONS = {'txt'}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app=app)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from flaskr import text, image, pdf
    app.register_blueprint(text.bp)
    app.register_blueprint(image.bp)
    app.register_blueprint(pdf.bp)
    return app
