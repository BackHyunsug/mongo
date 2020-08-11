from pymongo import MongoClient

conn = MongoClient("mongodb://test:1234@127.0.0.1:27017/")

#디비연결자를 통해서 데이터베이스 가져오기 
db = conn.mydb 

def member_list():
    collections = db.member.find()
    for member in collections:
        #print(type(member))
        print(member["_id"], member["member_id"])

def create_guestbook():
    #새로운 컬렉션 만들기 
    guestbook = db.guestbook
    #remove 앞으로 없어질 예정임 
    guestbook.delete_many({})#조건을 만족하는 거는 삭제하라-전부삭제
    guestbook.insert_one({'id':1, 'title':'제목1', 'writer':'방문객1'})
    guestbook.insert_one({'id':2, 'title':'제목2', 'writer':'방문객2'})
    guestbook.insert_one({'id':3, 'title':'제목3', 'writer':'방문객3'})
    
def guestbook_list():
    guestbook = db.guestbook    #2, '2'
    key = int(input("찾을 값 : "))
    collections = guestbook.find({'id':key})
    
    rows = list(collections)#일반적인 list 가 아니고 
    #우리가 데이터를  읽어오기위한 커서를 전달한다 
    #커서가 하나의 데이터를 읽고 나면 다음으로 이동한다 
    print("{} 개 찾았습니다. ".format(len(rows)))
    for row in rows:
        print(type(row), row)


#create_guestbook() 
guestbook_list() #함수실행

#업데이트 
def guestbook_update():
    #수정하기 
    #find_one_and_update(조건식, 업데이트할내용)
    #                   ({키:변수}, {'$set':{'title':변수, }})
    # guestbook컬렉션의 1번요소의 title을 제목1에서 수정으로 바꿔보자 
    db.guestbook.find_one_and_update({'id':1},
               {'$set':{'title':'수정', 'writer':'홍길동'}})

def guestbook_delete():
    db.guestbook.delete_one({'id':1})

guestbook_delete()

#guestbook_update()
#guestbook_list() #함수실행

#자동증가시퀀스 
"""
db.createCollection("customSequences")
db.customSequences.insert({"_id":"guestbook", "seq":0})
mongo안에서 
"""

#키에 해당되는 시퀀스를 자동 증가시키고 그 값을 반환하는 함수 
def getSequence(key):
    #find_one_and_update( 조건식 json,  업데이트연산 json, 옵션)
    #return_document  속성이 True 이어야 값을 수정후 수정된 객체를 
    #반환한다 
    doc = db.customSequences.find_one_and_update(
        {"_id":key}, {"$inc":{"seq":1}}, 
        return_document=True 
    )
    print(doc)
    return doc['seq']

# print(   getSequence("guestbook") )
# print(   getSequence("guestbook") )
# print(   getSequence("guestbook") )

def guestbook_insert():
    title = input("제목 : ")
    writer = input("작성자 : ")

    id = getSequence("guestbook")
    db.guestbook.insert_one({'id':id, 'title':title, 'writer':writer})

guestbook_insert()
guestbook_list()


