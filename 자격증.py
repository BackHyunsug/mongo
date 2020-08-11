from pymongo import MongoClient

class License:
    connString = "mongodb://test:1234@127.0.0.1:27017/"
    conn = MongoClient(connString)
    data = list() #클래스 정의될때딱 한번 
    def __init__(self):
        #self.data = list()#객체 생성될때마다 
        self.license=self.conn.mydb.license 

    def getSequence(self, key):
        doc = self.conn.mydb.customSequences.find_one_and_update(
            {"_id":key}, {"$inc":{"seq":1}}, 
            return_document=True 
        )
        print(doc)
        return doc['seq']

    def insert(self):
        name = input("이름 : ")
        structure = input("자료구조 : ")
        software = input("소프트웨어 : ")
        information=input("정보 : ")
        database = input("데이터베이스 : ")

        data = {'name':name, 'structure':structure, 'software':software,
                'information':information, 'database':database, 
                'id':self.getSequence("information")}
        """
        db.customSequences.insert({"_id":"information", "seq":0})
        db.license.find()
        """
        print( data )
        self.license.insert_one(data)

    def output(self):
        pass 

license = License()
license.insert()
license.output()


    



