#pip install pymongo

from pymongo import MongoClient
from pymongo.cursor import CursorType


# 접속 함수
def connect():
    client = MongoClient("mongodb://localhost:27017")
    return client

# 접속 테스트
def test_connect():
    conn = connect()
    # print(dir(conn))
    print("데이터베이스 : ")
    for db in conn.list_database_names():
        print(db)

# 컬렉션 확인
def test_collection():
    # 접속
    conn = connect()
    # 사용할 데이터베이스 선택
    db = conn['miniproject1']
    # 컬렉션 선택
    coll = db['phone_book']
    return coll





if __name__ == "__main__":
    # connect()
    # test_connect()
    test_collection()