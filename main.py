from flask import Flask
from flask_cors import CORS
from mongoengine import connect

from loggings.Log import setup_logging_to_file
from routes.Admin import admin

setup_logging_to_file('loggings/temp_log.txt')

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.config['ADMIN_FOLDER'] = app.root_path + 'frontend-admin/build/'
app.config['WEB_FOLDER'] = app.root_path + 'frontend/build/'
app.config['UPLOAD_FOLDER'] = app.root_path
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

ALLOWED_EXTENSIONS = {'png', 'jpg'}

app.register_blueprint(admin, url_prefix='/admin')

connect('blogsite')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
