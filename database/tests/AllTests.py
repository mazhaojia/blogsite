import unittest

from database.tests.BlogTests import BlogTests
from database.tests.CategoryTests import CategoryTests


def suite():
    category_suite = CategoryTests.suite()
    blog_suite = BlogTests.suite()
    all_tests = unittest.TestSuite((blog_suite, category_suite))
    return all_tests


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
