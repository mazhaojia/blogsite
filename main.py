import logging

from flask import Flask
from flask_cors import CORS

logging.basicConfig(format='%(message)s')

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = app.root_path
ALLOWED_EXTENSIONS = {'png'}


@app.route('/')
def home():
    return app.send_static_file('web/index.html')


@app.route('/upload/file/png', methods=['POST'])
def process():
    pass


if __name__ == "__main__":
    app.run()
