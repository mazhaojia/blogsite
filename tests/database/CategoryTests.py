import unittest

from mongoengine import connect, disconnect

from database.models.Category import Category
from database.operations.CategoryOperations import CategoryOperations


class CategoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect('blogsite')

    @classmethod
    def tearDownClass(cls):
        CategoryOperations.delete('test1')
        CategoryOperations.delete('test2')
        CategoryOperations.delete('test3')
        disconnect()

    def test_0_addCategory(self):
        CategoryOperations.add('test1')
        categories = Category.objects(name='test1')
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'test1')

        CategoryOperations.add('test2')
        categories = Category.objects(name='test2')
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'test2')

    def test_1_deleteCategory(self):
        CategoryOperations.delete('test1')
        categories = Category.objects(name='test1')
        self.assertEqual(len(categories), 0)

        CategoryOperations.delete('test2')
        categories = Category.objects(name='test2')
        self.assertEqual(len(categories), 0)

    def test_2_getCategory(self):
        CategoryOperations.get_category('test3')
        categories = Category.objects(name='test3')
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'test3')

        CategoryOperations.get_category('test3')
        categories = Category.objects(name='test3')
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'test3')

        CategoryOperations.delete('test3')

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTests([CategoryTests('test_0_addCategory'), CategoryTests('test_1_deleteCategory'), CategoryTests('test_2_getCategory')])
        return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(CategoryTests.suite())
