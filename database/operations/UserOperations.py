import hashlib
import os

from database.models.User import User


class UserOperations:
    @staticmethod
    def add(phone, username, password):
        hashed = hashlib.sha512()
        hashed.update(password.encode('utf-8'))
        user = User(phone=phone, username=username, password=hashed.hexdigest())
        user.save()

    @staticmethod
    def delete(phone):
        users = User.objects(phone=phone)
        if len(users) == 1:
            user = users.first()
            user.delete()

    @staticmethod
    def modify_password(phone, new_password):
        users = User.objects(phone=phone)
        if len(users) == 1:
            user = users.first()
            hashed = hashlib.sha512()
            hashed.update(new_password.encode('utf-8'))
            user.password = hashed.hexdigest()
            user.save()

    @staticmethod
    def verify_password(phone, password):
        users = User.objects(phone=phone)
        if len(users) == 1:
            user = users.first()
            hashed = hashlib.sha512()
            hashed.update(password.encode('utf-8'))
            if user.password == hashed.hexdigest():
                return True
        return False

    @staticmethod
    def modify_phone(_id, new_phone):
        users = User.objects(id=_id)
        if len(users) == 1:
            user = users.first()
            user.phone = new_phone
            user.save()

    @staticmethod
    def modify_user(phone, username, picture_path):
        users = User.objects(phone=phone)
        if len(users) == 1:
            user = users.first()
            user.username = username
            if user.picture_path is not None:
                if os.path.isfile(user.picture_path):
                    os.remove(user.picture_path)
            user.picture_path = picture_path
            user.save()
