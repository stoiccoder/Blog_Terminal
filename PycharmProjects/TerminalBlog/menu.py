from database import Database
from models.blog import Blog


class Menu:
    def __init__(self):
        self.user = input("Enter your user name: ")
        self.user_blog=None
        if self._user_has_account():
            print("Welcome {}".format(self.user+" !"))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {"author": self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        print("New User? Creating account...")
        title = input("Enter title for your blog: ")
        description = input("A brief description of your blog: ")
        while(1):
            id = input("Enter a unique id for your blog: ")
            if not self._is_unique(id):
                print("Someone already has that id. Please choose a unique id.")
            else:
                break
        blog = Blog(self.user, title, description, id)
        blog.save_to_mongo()
        self.user_blog = blog

    @staticmethod
    def _is_unique(id1):
        blogs = Database.find("blogs", {})
        for blog in blogs:
            if blog['id']==id1:
                return False
        return True

    def run_menu(self):
        while(True):
            check = input("Read(R) or Write(W)? Any other key to exit. ")
            if check=="R" or check=="r":
                self._list_blogs()
                self._view_blog()

            elif check=="W" or check=="w":
                self.user_blog.new_post()
            else:
                print("Bye!")
                break

    def _list_blogs(self):
        blogs = Database.find("blogs", {})
        if blogs is None or blogs=="" :
            print("Database is empty!")
            return
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter blog ID to see ")
        try:
            blog = Blog.from_mongo(blog_to_see)
            posts = blog.get_posts()
        except:
            print("No such Post exists.")
            return
        if posts is None or posts==[]:
            print("No posts in the blog.")
            return
        for post in posts:
            print("Date: {}, Title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
