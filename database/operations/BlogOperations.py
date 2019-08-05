from datetime import datetime

from database.models.Blog import Blog
from database.models.Comment import Comment
from database.models.Reply import Reply
from database.operations.CategoryOperations import CategoryOperations


class BlogOperations:
    # blog
    @staticmethod
    def add(category_name, title, content):
        category = CategoryOperations.get_category(category_name)
        published_datetime = datetime.utcnow()
        blog = Blog(category=category, title=title, content=content, published_dateTime=published_datetime)
        blog.save()

    @staticmethod
    def delete(blog_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            blog.delete()

    @staticmethod
    def like(blog_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.likes is None:
                blog.likes = 0
            blog.likes += 1
            blog.save()

    @staticmethod
    def dislike(blog_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.dislikes is None:
                blog.dislikes = 0
            blog.dislikes += 1
            blog.save()

    @staticmethod
    def user_viewed(blog_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.viewed_numbers is None:
                blog.viewed_numbers = 0
            blog.viewed_numbers += 1
            blog.save()

    @staticmethod
    def modify(blog_id, category_name, title, content):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            blog.category.name = category_name
            blog.title = title
            blog.content = content
            blog.last_modified_dateTime = datetime.utcnow()
            blog.save()

    @staticmethod
    def add_tag(blog_id, name):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.tags is None:
                blog.tags = []
            blog.tags.append(name)
            blog.save()

    @staticmethod
    def delete_tag(blog_id, name):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.tags is not None:
                blog.tags.remove(name)
                blog.save()

    # comment
    @staticmethod
    def add_comment(blog_id, username, content):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            comment = Comment(username=username, content=content, published_datetime=datetime.utcnow())
            if blog.comments is None:
                blog.comments = []
            blog.comments.insert(0, comment)
            blog.save()

    @staticmethod
    def delete_comment(blog_id, comment_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    blog.comments.pop(idx)
                    blog.save()

    @staticmethod
    def like_comment(blog_id, comment_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    if blog.comments[idx].likes is None:
                        blog.comments[idx].likes = 0
                    blog.comments[idx].likes += 1
                    blog.save()

    @staticmethod
    def dislike_comment(blog_id, comment_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    if blog.comments[idx].dislikes is None:
                        blog.comments[idx].dislikes = 0
                    blog.comments[idx].dislikes += 1
                    blog.save()

    # reply
    @staticmethod
    def add_reply(blog_id, comment_id, username, content):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    reply = Reply(username=username, content=content, published_datetime=datetime.utcnow())
                    if blog.comments[idx].replies is None:
                        blog.comments[idx].replies = []
                    blog.comments[idx].replies.append(reply)
                    blog.save()

    @staticmethod
    def delete_reply(blog_id, comment_id, reply_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    idx2 = -1
                    for index, item in enumerate(blog.comments[idx].replies):
                        if item.oid == reply_id:
                            idx2 = index
                            break
                    if idx2 != -1:
                        blog.comments[idx].replies.pop(idx2)
                        blog.save()

    @staticmethod
    def like_reply(blog_id, comment_id, reply_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    idx2 = -1
                    for index, item in enumerate(blog.comments[idx].replies):
                        if item.oid == reply_id:
                            idx2 = index
                            break
                    if idx2 != -1:
                        if blog.comments[idx].replies[idx2].likes is None:
                            blog.comments[idx].replies[idx2].likes = 0
                        blog.comments[idx].replies[idx2].likes += 1
                        blog.save()

    @staticmethod
    def dislike_reply(blog_id, comment_id, reply_id):
        blogs = Blog.objects(id=blog_id)
        if len(blogs) == 1:
            blog = blogs.first()
            if blog.comments is not None:
                idx = -1
                for index, item in enumerate(blog.comments):
                    if item.oid == comment_id:
                        idx = index
                        break
                if idx != -1:
                    idx2 = -1
                    for index, item in enumerate(blog.comments[idx].replies):
                        if item.oid == reply_id:
                            idx2 = index
                            break
                    if idx2 != -1:
                        if blog.comments[idx].replies[idx2].dislikes is None:
                            blog.comments[idx].replies[idx2].dislikes = 0
                        blog.comments[idx].replies[idx2].dislikes += 1
                        blog.save()
