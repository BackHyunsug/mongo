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

    def process(self,row):
        total = int(row['structure']) + int(row['software']) + \
                   int(row['information'])+int(row['database'])
        avg = total/4
        if avg <60:
            grade="불합격"
        else:
            if int(row['structure'])<40 or \
                int(row['software'])<40 or \
                int(row['information'])<40 or \
                int(row['database'])<40 : 
                grade="과락"
            else:
                grade="합격"
        return total, avg, grade 

    def output(self):
        cursor = self.license.find()
        for row in cursor:
            total, avg, grade = self.process(row)
            print(row['name'], total, avg, grade)

    def search(self):
        key = input('찾을 이름은? ')
        cursor = self.license.find({"name":key})
        result = list(cursor)
        if len(result)>0:
            for row in result:
                total, avg, grade = self.process(row)
                print(row['name'], total, avg, grade)
        else:
            print("찾으시는 이름이 없습니다.")
    
    def modify(self):
        name = input("이름 : ")
        structure = input("자료구조 : ")
        software = input("소프트웨어 : ")
        information=input("정보 : ")
        database = input("데이터베이스 : ")

        data = {'name':name, 'structure':structure, 'software':software,
                'information':information, 'database':database}
     
        self.license.find_one_and_update({'name':name},
               {'$set': data })

    def delete(self):
        key = input('찾을 이름은? ')
        cursor = self.license.find({"name":key})
        result = list(cursor)
        if len(result)>0:
            self.license.delete_one({"name":key})
        else:
            print("찾으시는 이름이 없습니다.")

license = License()
#license.insert()
#license.modify()
license.delete()
license.output()
#license.search()



    



