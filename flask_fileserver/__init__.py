import os.path
from flask import Flask
from flask_autoindex import AutoIndex

def create_app(browse_root_dir=None):
     app = Flask(__name__)
     AutoIndex(app, browse_root=browse_root_dir.as_posix())
     return app