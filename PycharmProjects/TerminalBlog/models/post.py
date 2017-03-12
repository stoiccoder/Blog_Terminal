import uuid
from database import Database
from datetime import datetime


class Post:

    def __init__(self, title, author, content, blog_id, date=datetime.now(), id=None):
        self.title = title
        self.blog_id = blog_id
        self.author = author
        self.content = content
        self.id = uuid.uuid4().hex if id is None else id       # uuid4 is for random
        self.created_date = date

    def json(self):
        return{
            "id": self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            "author": self.author,
            "content": self.content,
            "created_date": self.created_date
        }

    def save_to_mongo(self):
        Database.insert(collection="posts", data=self.json())

    @staticmethod
    def from_mongo(id):
        return Database.find(collection="posts", query={"id": id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]
