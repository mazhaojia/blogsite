import unittest

from mongoengine import connect, disconnect

from database.models.Blog import Blog
from database.operations.BlogOperations import BlogOperations
from database.operations.CategoryOperations import CategoryOperations


class BlogTests(unittest.TestCase):
    saved_id = None

    @classmethod
    def setUpClass(cls):
        connect('blogsite')

    @classmethod
    def tearDownClass(cls):
        CategoryOperations.delete('test')
        disconnect()

    def test_00_add(self):
        BlogOperations.add(category_name='test', title='title', content='content')
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs), 1)
        BlogTests.saved_id = blogs[0].id

    def test_01_like(self):
        BlogOperations.like(BlogTests.saved_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(blogs[0].likes, 1)

    def test_02_dislike(self):
        BlogOperations.dislike(BlogTests.saved_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(blogs[0].dislikes, 1)

    def test_03_userViewed(self):
        BlogOperations.user_viewed(BlogTests.saved_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(blogs[0].viewed_numbers, 1)

    def test_04_addTag(self):
        BlogOperations.add_tag(BlogTests.saved_id, 'new_tag')
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].tags), 1)
        self.assertEqual(blogs[0].tags[0], 'new_tag')

    def test_05_deleteTag(self):
        BlogOperations.delete_tag(BlogTests.saved_id, 'new_tag')
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].tags), 0)

    def test_06_addComment(self):
        BlogOperations.add_comment(BlogTests.saved_id, 'anonymous', 'very good comment')
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments), 1)
        self.assertEqual(blogs[0].comments[0].username, 'anonymous')
        self.assertEqual(blogs[0].comments[0].content, 'very good comment')
        BlogTests.saved_comment_id = blogs[0].comments[0].oid

    def test_07_likeComment(self):
        BlogOperations.like_comment(BlogTests.saved_id, BlogTests.saved_comment_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments), 1)
        self.assertEqual(blogs[0].comments[0].likes, 1)

    def test_08_dislikeComment(self):
        BlogOperations.dislike_comment(BlogTests.saved_id, BlogTests.saved_comment_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments), 1)
        self.assertEqual(blogs[0].comments[0].dislikes, 1)

    def test_09_addReply(self):
        BlogOperations.add_reply(BlogTests.saved_id, BlogTests.saved_comment_id, 'anonymous', 'very good reply')
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments[0].replies), 1)
        self.assertEqual(blogs[0].comments[0].replies[0].username, 'anonymous')
        self.assertEqual(blogs[0].comments[0].replies[0].content, 'very good reply')
        BlogTests.saved_reply_id = blogs[0].comments[0].replies[0].oid

    def test_10_likeReply(self):
        BlogOperations.like_reply(BlogTests.saved_id, BlogTests.saved_comment_id, BlogTests.saved_reply_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments[0].replies), 1)
        self.assertEqual(blogs[0].comments[0].replies[0].likes, 1)

    def test_11_dislikeReply(self):
        BlogOperations.dislike_reply(BlogTests.saved_id, BlogTests.saved_comment_id, BlogTests.saved_reply_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments[0].replies), 1)
        self.assertEqual(blogs[0].comments[0].replies[0].dislikes, 1)

    def test_12_deleteReply(self):
        BlogOperations.delete_reply(BlogTests.saved_id, BlogTests.saved_comment_id, BlogTests.saved_reply_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments[0].replies), 0)

    def test_13_deleteComment(self):
        BlogOperations.delete_comment(BlogTests.saved_id, BlogTests.saved_comment_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs[0].comments), 0)

    def test_14_delete(self):
        BlogOperations.delete(BlogTests.saved_id)
        blogs = Blog.objects(title='title')
        self.assertEqual(len(blogs), 0)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTests([BlogTests('test_00_add'), BlogTests('test_01_like'), BlogTests('test_02_dislike'),
                        BlogTests('test_03_userViewed'), BlogTests('test_04_addTag'), BlogTests('test_05_deleteTag'),
                        BlogTests('test_06_addComment'), BlogTests('test_07_likeComment'), BlogTests('test_08_dislikeComment'),
                        BlogTests('test_09_addReply'), BlogTests('test_10_likeReply'), BlogTests('test_11_dislikeReply'),
                        BlogTests('test_12_deleteReply'), BlogTests('test_13_deleteComment'), BlogTests('test_14_delete')])
        return suite


if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = None
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(BlogTests.suite())
