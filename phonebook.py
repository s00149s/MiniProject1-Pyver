# 모듈 임포트
import sqlite3, os
from sqlite3 import Error


def create_connection(db_file):
    if not os.path.exists("./database"):
        os.makedirs("./database")

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e, type(e))
        return None
    return conn

    conn = create_connection(db_file)
    cursor = conn.cursor()









if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    create_connection(db_file)


