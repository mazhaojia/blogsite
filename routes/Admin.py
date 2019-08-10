from datetime import datetime

from flask import Blueprint, request, make_response, jsonify, send_from_directory, current_app
from werkzeug.utils import redirect

from controllers.Admin import Admin

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin_home():
    token = request.cookies.get('login')
    if Admin.verify_token(token):
        return send_from_directory(current_app.config['ADMIN_FOLDER'], 'index.html')
    return redirect('/admin/login')


@admin.route('/login', method=['GET'])
def admin_login_get():
    return send_from_directory(current_app.config['ADMIN_FOLDER'], 'login.html')


@admin.route('/login', methods=['POST'])
def admin_login_post():
    password = request.json['password']
    if Admin.login(password):
        token = Admin.get_token()
        expire_date = datetime.datetime.now() + datetime.timedelta(days=7)
        max_age = 7 * 60 * 60 * 24
        response = make_response(jsonify(success=True, token=token))
        response.set_cookie(key='login', value=token, max_age=max_age, expires=expire_date)
        return response
    return jsonify(success=False)
