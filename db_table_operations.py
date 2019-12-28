import os
import sys
import psycopg2 as dbapi2

# USER AUTHENTICATION TABLE OPERATIONS #
def insert_user(object):
    query ='INSERT INTO USERS (USERNAME, NAME, SURNAME, EMAIL, PASSWORD, AGE, GENDER) ' \
           'VALUES(%s, %s, %s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        # hash the password
        print("User pw:" + object.password)
        cursor.execute(query, (object.username, object.name, object.surname, object.email,
                               object.password, object.age, object.gender))
        # print("User pw:" + object.password.decode("utf-8"))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()


def find_user_by_username(username):
    query = "SELECT * FROM USERS WHERE USERNAME = %s"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        rows_count = cursor.execute(query,(username,))
        print("User is found in DB")
        found_user = cursor.fetchone()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return found_user


def find_user_by_id(id):
    query = "SELECT * FROM USERS WHERE ID = %s"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        rows_count = cursor.execute(query,(id,))
        print("User is found in DB")
        found_user = cursor.fetchone()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return found_user


def check_password(user_password, form_password):
    # compare the passwords
    return user_password==form_password

# USER LIST OPERATIONS
def userlist_add_book(user_id, book_id):
    query = 'INSERT INTO BOOK_LIST (USER_ID, BOOK_ID) VALUES(%s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id, book_id))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id

def userlist_add_poem(user_id, poem_id):
    query = 'INSERT INTO POEM_LIST (USER_ID, POEM_ID) VALUES(%s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id, poem_id))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id
def userlist_get_poems():
    query ='SELECT POEM.* FROM POEM_LIST ' \
           'INNER JOIN POEM ON POEM_LIST.POEM_ID = POEM.ID ' \
           'INNER JOIN USERS ON POEM_LIST.USER_ID = USERS.ID'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        poems = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return poems
        # return id

def userlist_get_books():
    query ='SELECT BOOK.* FROM BOOK_LIST ' \
           'INNER JOIN BOOK ON BOOK_LIST.BOOK_ID = BOOK.ID ' \
           'INNER JOIN USERS ON BOOK_LIST.USER_ID = USERS.ID'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        books = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return books
        # return id


def userlist_delete_poem(user_id, poem_id):
    query = "DELETE FROM POEM_LIST WHERE USER_ID = CAST(%s AS INTEGER) AND POEM_ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id, poem_id))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("poem with id " + poem_id + " from user with id " + user_id + " deleted")
        # return id


def userlist_delete_book(user_id, book_id):
    query = "DELETE FROM BOOK_LIST WHERE USER_ID = CAST(%s AS INTEGER) AND BOOK_ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id, book_id))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("book with id " + book_id + " from user with id " + user_id + " deleted")
        # return id

# BOOK TABLE OPERATIONS #
def get_books():
    query ='SELECT * FROM BOOK'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        poems = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return poems
        # return id


def insert_book(book):
    query ='INSERT INTO BOOK (NAME, AUTHOR, NUMBER_OF_PAGES, PUBLISHER, CATEGORY) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (book.name, book.author, book.number_of_pages,
                               book.publisher, book.category))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id


def update_book(book_id, book):
    query = "UPDATE BOOK " \
            "SET NAME = %s, " \
            "AUTHOR = %s, " \
            "NUMBER_OF_PAGES = %s, " \
            "PUBLISHER = %s, " \
            "CATEGORY = %s " \
            "WHERE ID = %s "
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (book.name, book.author, book.number_of_pages,
                               book.publisher, book.category, book_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("book with id " + book_id + " deleted")
        # return id
        
def delete_book(book_id):
    query = "DELETE FROM BOOK WHERE ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (book_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("book with id " + book_id + " deleted")
        # return id

# POEM TABLE OPERATIONS #
def get_poems():
    query ='SELECT * FROM POEM'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        poems = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return poems
        # return id


def insert_poem(poem):
    query ='INSERT INTO POEM(TITLE, YEAR, CONTENT, AUTHOR, CATEGORY) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (poem.title, poem.year, poem.content, poem.author, poem.category))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id

def update_poem(poem_id, poem):
    query = "UPDATE POEM " \
            "SET TITLE = %s, " \
            "YEAR = %s, " \
            "CONTENT = %s, " \
            "AUTHOR = %s, " \
            "CATEGORY = %s " \
            "WHERE ID = %s "
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (poem.title, poem.year, poem.content,
                              poem.author, poem.category, poem_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("poem with id " + poem_id + " deleted")
        # return id


def delete_poem(poem_id):
    query = "DELETE FROM POEM WHERE ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (poem_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("poem with id " + poem_id + " deleted")
        # return id
def get_db_url():
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    return url
