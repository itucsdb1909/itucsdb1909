import os
import sys

import psycopg2 as dbapi2
import db_table_operations as tab

INIT_STATEMENTS = [
    "DROP TABLE IF EXISTS USERS CASCADE", # to test changes quickly
    "DROP TABLE IF EXISTS BOOK CASCADE",
    "DROP TABLE IF EXISTS POEM CASCADE",
    "DROP TABLE IF EXISTS BOOK_LIST CASCADE",
    "DROP TABLE IF EXISTS POEM_LIST CASCADE",

    "CREATE TABLE IF NOT EXISTS USERS("
        "ID SERIAL,"
        "USERNAME VARCHAR(50) NOT NULL,"
        "NAME VARCHAR(50),"
        "SURNAME VARCHAR(50),"
        "EMAIL VARCHAR(50),"
        "PASSWORD VARCHAR(20),"
        "AGE VARCHAR(3),"
        "GENDER VARCHAR(5),"
        "PRIMARY KEY(ID)"
#        "CONSTRAINT id_fkey_book FOREIGN KEY (ID) REFERENCES BOOK_LIST(USER_ID)," 
#        "CONSTRAINT id_fkey_poem FOREIGN KEY (ID) REFERENCES POEM_LIST(USER_ID)"
    ")",
    
    "CREATE TABLE IF NOT EXISTS BOOK("
    "ID SERIAL,"  
    "NAME VARCHAR(50),"
    "AUTHOR VARCHAR(50),"
    "NUMBER_OF_PAGES VARCHAR(4),"
    "PUBLISHER VARCHAR(50),"
    "CATEGORY VARCHAR(50),"
    "PRIMARY KEY(ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS POEM("
    "ID SERIAL," 
    "TITLE VARCHAR(50),"
    "YEAR VARCHAR(4),"
    "CONTENT VARCHAR(1000),"
    "AUTHOR VARCHAR(50),"
    "CATEGORY VARCHAR(50),"
    "PRIMARY KEY(ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS BOOK_LIST("
    "USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,"
    "BOOK_ID INTEGER REFERENCES BOOK(id) ON DELETE CASCADE,"
    "PRIMARY KEY(USER_ID, BOOK_ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS POEM_LIST("
    "USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,"
    "POEM_ID INTEGER REFERENCES POEM(id) ON DELETE CASCADE,"
    "PRIMARY KEY(USER_ID, POEM_ID)"
    ")",

    # user references _list's USER_ID too.

    # "INSERT INTO DUMMY VALUES (42)",
    # "   USERNAME VARCHAR(50)"
    # "   NAME VARCHAR(50)"
    # "   SURNAME VARCHAR(50)"
    # "   PASSWORD VARCHAR(20)"
    # "   AGE INTEGER"
    # "   )",
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
    # tab.insert_user("username", "name", "surname", "password", 70, "gender")
# jdbc:postgresql://localhost:32768/itucsdb
