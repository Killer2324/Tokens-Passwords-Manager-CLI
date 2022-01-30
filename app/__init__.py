import sys
from dotenv import load_dotenv
import os
from db import Database

def create_app():
    load_dotenv()
    database = Database(
        os.environ.get("DATABASE"),
        os.environ.get("USER"),
        os.environ.get("PASSWORD"),
        os.environ.get("HOST")
    )

    ask_to_user(database)
    print("\nThanks for use this application.")

def ask_to_user(database):
    print("Hi, I'm your assistant.")
    print("\nOptions:")
    print("\n 1. Insert a new Password or Token \n 2. See my Tokens/Passwords \n 3. Delete All \n 4. Update one Content")
    query = input("Choose one: ")

    if query == '1':
        name = input("Password/Token Name: ")
        content = input("Password/Token Content: ")
        insert_to_db(database, name, content)

        query2 = input("Do you want to insert something else? (Y/n)")
        if query2 == 'Y' or query2 == 'y':
            ask_to_user(database)
        else:
            sys.exit()

    elif query == '2':
        show_passwords(database)
    elif query == '3':
        delete_all_passwords(database)
    elif query == '4':
        show_passwords(database)
        name = input("What token/password do you want to change? (put the 'token/password name') ")
        content = input("Ok, set the new content: ")
        update_content_passwords(database, name, content)

def insert_to_db(database, name, content):
    database.insert(name, content)

def show_passwords(database):
    database.show()

def delete_all_passwords(database):
    database.delete_all()

def update_content_passwords(database, name, new_content):
    database.update_content(name, new_content)
if __name__ == '__main__':
    create_app()