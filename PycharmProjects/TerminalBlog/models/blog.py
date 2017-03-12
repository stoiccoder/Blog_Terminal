import uuid
from datetime import datetime
from database import Database
from models.post import Post


class Blog:
    def __init__(self, author, title="No Title.", description="No description.", id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id= id

    def new_post(self):
        title = input("Enter post title: ")
        print("Enter post content...(Blank line to end.)\n")
        lines=[]
        while(True):
            line=input()
            if line:
                lines.append(line)
            else:
                break
        content="\n".join(lines)
        date = input("Enter date in DDMMYYYY format or else leave blank for today: ")
        if date == "":
            date = datetime.now()
        else:
            date = datetime.strptime(date, "%d%m%Y")
        post = Post(title=title,
                    author=self.author,
                    content=content,
                    blog_id=self.id,
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert("blogs", self.json())

    def json(self):
        return{
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data=Database.find_one("blogs", {"id": id})
        return cls(author=blog_data["author"],
                   title=blog_data["title"],
                   description=blog_data["description"],
                   id=blog_data["id"])



