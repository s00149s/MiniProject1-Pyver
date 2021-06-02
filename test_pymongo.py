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

def print_menu():
    while True:
        print("***************************************")
        print("*         전화번호 관리 프로그램          *")
        print("***************************************")
        print("1.리스트 2.등록 3.삭제 4.검색 5.종료")
        print("---------------------------------------")
        print(">메뉴번호 : ")
        num = int(input())
        if num == 1:
            test_list()
        elif num == 2:
            test_insert()
        elif num == 3:
            test_delete_by_filter()
        elif num == 4:
            test_select_by_filter()
        elif num == 5:
            print("***************************************")
            print("*              감사합니다               *")
            print("***************************************")
            break
        else:
            print("[다시 입력해 주세요.]")





def test_list(projection={}):
    print("<1.리스트>")
    coll = test_collection()
    docs = coll.find(projection={"name":1, "hp":1, "tel":1, "_id":0})
    for x in docs:
        print(x)




def test_insert():
    coll = test_collection()
    print("<2.등록>")
    name = input(">이름: ")
    hp = input(">휴대전화: ")
    tel = input(">집전화: ")

    x = coll.insert_one({
        "name" : name,
        "hp" : hp,
        "tel" : tel
    })
    print("[등록되었습니다.]")



def test_select_by_filter(filter={}, projection={}):
    """
    db.collection.find({ 조건 }, { projection })
        프로젝션 값은 1 표시, 값 0: 표시안함
    """
    coll = test_collection()
    docs = coll.find_one(filter, projection)

    for doc in docs:
        print(doc)

def test_delete_by_filter(filter={}):
    coll = test_collection()
    xs = coll.delete_one(filter)
    print("[삭제되었습니다.]")



if __name__ == "__main__":
    # connect()
    # test_connect()
    # test_collection()
    # test_insert()
    # test_select_by_filter(projection={
    #     "name" : 1,
    #     "hp" : 1,
    #     "tel" : 1,
    #     "_id": 0
    # })
    # test_list()
    print_menu()