import logging
from flask import Flask
from flask_cors import CORS

from logging.Log import setup_logging_to_file
from routes.Admin import admin

setup_logging_to_file('logging/temp_log.txt')

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = app.root_path
ALLOWED_EXTENSIONS = {'png', 'jpg'}

app.register_blueprint(admin, url_prefix='/admin')

if __name__ == "__main__":
    app.run(debug=True)
