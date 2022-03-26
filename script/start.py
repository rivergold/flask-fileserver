import sys
sys.path.append('.')
from argparse import ArgumentParser
from flask_fileserver import create_app
from rutils.common import str2path

if __name__ == '__main__':
    opt_parser = ArgumentParser()
    opt_parser.add_argument('-i',
                            '--browse_root_dir',
                            type=str2path,
                            required=True)
    opt_parser.add_argument('-u', '--upload_dir', type=str2path, required=True)
    opt = opt_parser.parse_args()

    app = create_app(browse_root_dir=opt.browse_root_dir,
                     upload_dir=opt.upload_dir)
    app.run()
