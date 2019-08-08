import unittest

from mongoengine import connect, disconnect

from database.models.User import User
from database.operations.UserOperations import UserOperations


class UserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect('blogsite')

    @classmethod
    def tearDownClass(cls):
        UserOperations.delete('17605123977')
        disconnect()

    def test_60_addUser(self):
        UserOperations.add('17605123977', 'muffin', 'nopassword')
        users = User.objects(phone='17605123977')
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'muffin')
        UserTests.saved_id = users[0].id
        UserTests.saved_password = users[0].password

    def test_61_modifyUser(self):
        UserOperations.modify_user('17605123977', 'marvin', 'web/my.png')
        users = User.objects(phone='17605123977')
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'marvin')
        self.assertEqual(users[0].picture_path, 'web/my.png')

    def test_62_modifyPassword(self):
        UserOperations.modify_password('17605123977', 'new_password')
        users = User.objects(phone='17605123977')
        self.assertEqual(len(users), 1)
        self.assertNotEqual(users[0].password, UserTests.saved_password)

    def test_63_verifyPassword(self):
        self.assertTrue(UserOperations.verify_password('17605123977', 'new_password'))

    def test_64_modifyPhone(self):
        UserOperations.modify_phone(UserTests.saved_id, '15850208731')
        users = User.objects(id=UserTests.saved_id)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].phone, '15850208731')

    def test_65_deleteUser(self):
        UserOperations.delete('15850208731')
        users = User.objects(phone='15850208731')
        self.assertEqual(len(users), 0)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTests([UserTests('test_60_addUser'), UserTests('test_61_modifyUser'), UserTests('test_62_modifyPassword'),
                        UserTests('test_63_verifyPassword'), UserTests('test_64_modifyPhone'), UserTests('test_65_deleteUser')])
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(UserTests.suite())
