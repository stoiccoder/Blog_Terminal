# Blog_Terminal
A blogging application which can be run from the terminal window.
Uses a MongoDB server.
Multiple authors can exist. Each author can also have multiple blogs.
# Setup
Install MongoDB. https://www.mongodb.com/download-center?jmp=nav#community
Run the mongo server in the background.
Install packages from requirements.txt
Run the file app.py .
# Files
database.py - Initialising the database. Defining the insert and find methods
              to insert and fetch data from server.
menu.py - Defines the menu class which acts as the interacting medium between the user
          and the program.
blog.py/post.py - Define, respectively, the blog and post class.They are linked
                  through a unique blog_id. A blog contains multiple posts through
                  a single author.Though an author can have multiple blogs. Only contraint
                  is the blog_id which should be unique.
                  


