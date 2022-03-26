from crypt import methods
import os.path
from flask import Flask
from flask_autoindex import AutoIndex
from .route_func.upload import upload_file


def create_app(browse_root_dir=None, upload_dir=None):
    app = Flask(__name__)
    AutoIndex(app, browse_root=browse_root_dir.as_posix())
    app.config['upload_dir'] = upload_dir
    app.add_url_rule('/upload',
                     endpoint='upload',
                     view_func=upload_file,
                     methods=['GET', 'POST'])
    for rule in app.url_map.iter_rules():
        print(rule)
    return app
