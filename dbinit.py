import psycopg2 as dbapi2
dsn="""user='vagrant' password='vagrant'
host='localhost' port=5432 dbname='Anthology'"""
def initialize():
    init_statements=list()
    init_statements.append("""CREATE TABLE IF NOT EXISTS USERS(
        ID SERIAL,
        USERNAME VARCHAR(50) NOT NULL,
        NAME VARCHAR(50),
        SURNAME VARCHAR(50),
        EMAIL VARCHAR(50),
        PASSWORD VARCHAR(20),
        AGE VARCHAR(3),
        GENDER VARCHAR(5),
        PRIMARY KEY(ID))""")
    init_statements.append("""CREATE TABLE IF NOT EXISTS BOOK(
    ID SERIAL,
    NAME VARCHAR(50),
    AUTHOR VARCHAR(50),
    NUMBER_OF_PAGES VARCHAR(4),
    PUBLISHER VARCHAR(50),
    CATEGORY VARCHAR(50),
    PRIMARY KEY(ID))""")
    init_statements.append("""CREATE TABLE IF NOT EXISTS POEM(
    ID SERIAL,
    TITLE VARCHAR(50),
    YEAR VARCHAR(4),"
    CONTENT VARCHAR(1000),
    AUTHOR VARCHAR(50),
    CATEGORY VARCHAR(50),
    PRIMARY KEY(ID))""")
    init_statements.append("""CREATE TABLE IF NOT EXISTS BOOK_LIST(
    USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,
    BOOK_ID INTEGER REFERENCES BOOK(id) ON DELETE CASCADE,
    PRIMARY KEY(USER_ID, BOOK_ID))""")
    init_statements.append("""CREATE TABLE IF NOT EXISTS POEM_LIST(
    USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,
    POEM_ID INTEGER REFERENCES POEM(id) ON DELETE CASCADE,
    PRIMARY KEY(USER_ID, POEM_ID))""")
    connection=dbapi2.connect(dsn)
    cursor = connection.cursor()
    for statement in init_statements:
        cursor.execute(statement)
        connection.commit()
    cursor.close()
    connection.close()
