from datetime import datetime

from flask import Blueprint, request, make_response, jsonify, send_from_directory, current_app
from werkzeug.utils import redirect

from controllers.Admin import Admin

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
def admin_login():
    password = request.json['password']
    if Admin.login(password):
        token = Admin.get_token()
        expire_date = datetime.datetime.now() + datetime.timedelta(days=7)
        max_age = 7 * 60 * 60 * 24
        return jsonify(success=True, token=token, maxAge=max_age, expires=expire_date)
    return jsonify(success=False)
