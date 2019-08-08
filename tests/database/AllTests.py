import unittest

from tests.database.BlogTests import BlogTests
from tests.database.CategoryTests import CategoryTests
from tests.database.UserTests import UserTests


def suite():
    blog_suite = BlogTests.suite()
    category_suite = CategoryTests.suite()
    user_suite = UserTests.suite()
    all_tests = unittest.TestSuite((blog_suite, category_suite, user_suite))
    return all_tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
