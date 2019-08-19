from datetime import datetime
from pathlib import Path

import jwt
from jwt import PyJWTError

from database.operations.UserOperations import UserOperations
from loggings.Log import log_exception


def read_private_key():
    path = Path(__file__).resolve().parent.parent.joinpath('certs', 'private.key')
    with open(path) as file:
        return file.read()


class Admin:
    adminPhone = '17605123977'
    adminKey = read_private_key()

    @staticmethod
    def login(password):
        return UserOperations.verify_password(Admin.adminPhone, password)

    @staticmethod
    def get_token():
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        token = jwt.encode({'phone': Admin.adminPhone, 'exp': exp}, Admin.adminKey, algorithm='HS256')
        return token

    @staticmethod
    def verify_token(token):
        try:
            decoded = jwt.decode(token, Admin.adminKey, leeway=datetime.timedelta(hours=1), algorithms=['HS256'])
            if decoded['phone'] == Admin.adminPhone:
                return True
            return False
        except PyJWTError as e:
            log_exception(e)
            return False
