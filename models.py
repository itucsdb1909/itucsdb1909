from flask_login import UserMixin,LoginManager
from db_table_operations import find_user_by_id, find_user_by_username
def initialize_login():
    from server import login
    global login
    login=login

class User(UserMixin):
    initialize_login()

    def __init__(self, username, name, surname, email, password, age, gender):
        self.id = 0
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.age = int(age)
        self.gender = gender
        print("User object created")

    @login.user_loader
    def load_user(id):
        if id == 0:
            print("User not logged in, id is ", id)
            return
        else:
            found_user = find_user_by_id(int(id))
            return found_user

    def __repr__(self):
        return '<User %r>' % self.username

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id;

class Book:
    def __init__(self,name,author,number_of_pages,publisher,category):
        self.name= name
        self.author = author
        self.number_of_pages = number_of_pages
        self.publisher = publisher
        self.category = category
        print("Book object created")


class Poem:
    def __init__(self,title, year,content,author,category):
        self.title = title
        self.year = year
        self.content = content
        self.author = author
        self.category = category
        print("Poem object created")
