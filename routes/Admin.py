from datetime import datetime

from flask import Blueprint, request, app, make_response, jsonify
from werkzeug.utils import redirect

from controllers.Admin import Admin

admin = Blueprint('admin', __name__)


@admin.route('/')
def admin_home():
    token = request.cookies.get('login')
    if Admin.verify_token(token):
        return app.send_static_file('admin/index.html')
    return redirect('/admin/login')


@admin.route('/login', method=['GET'])
def admin_login_get():
    return app.send_static_file('admin/login.html')


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
