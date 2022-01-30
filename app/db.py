import mariadb
import sys
from schema import instruction

class Database:
    def __init__(self, database:str, user:str, password:str, host:str or int, port:int = 3306):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connect_db()
        self.create_table()

    def connect_db(self):
        try:
            conn = mariadb.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                database = self.database
            )
        except mariadb.Error as e:
            print(f"The connection had a error of type: {e}")
            sys.exit(1)
            

        cursor = conn.cursor()

        return conn, cursor

    def create_table(self):
        connection, cursor = self.connect_db()
        cursor.execute(instruction)
        connection.commit()
    
    def insert(self, name, content):
        connection, cursor = self.connect_db()
        cursor.execute(f"INSERT INTO passwords VALUES (null, '{name}', '{content}', CURTIME())")
        connection.commit()
        print("Perfect, Your Password have been registered")

    def show(self):
        connection, cursor = self.connect_db()

        names_list = []
        content_list = []
        dates_list = []

        cursor.execute("SELECT name FROM passwords")
        names = cursor.fetchall()
        
        cursor.execute("SELECT content FROM passwords")
        contents = cursor.fetchall()

        cursor.execute("SELECT created_at FROM passwords")
        dates = cursor.fetchall()

        for name in names:
            for name_value in name:
                names_list.append(name_value)

        for content in contents:
            for content_value in content:
                content_list.append(content_value)

        for date in dates:
            for date_value in date:
                dates_list.append(date_value)
                

        for name, content, date in zip(names_list, content_list, dates_list):
            print(f"\n name: {name}\n content: {content} \n date: {date}")
        connection.commit()