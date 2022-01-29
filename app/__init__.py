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
    print("\n 1. Insert a new API KEY")
    print("\n 2. See my API KEYS")
    query = input("Choose one: ")

    if (query == '1'):
        name = input("API Name: ")
        content = input("API Content: ")
        insert_to_db(database, name, content)
    else:
        show_keys(database)

def insert_to_db(database, name, content):
    database.insert(name, content)

def show_keys(database):
    database.show()

if __name__ == '__main__':
    create_app()