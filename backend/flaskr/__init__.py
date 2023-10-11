from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = 'images'
IMAGE_RESULT_FOLDER = 'utils'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


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

    from flaskr import text, image
    app.register_blueprint(text.bp)
    app.register_blueprint(image.bp)
    return app

