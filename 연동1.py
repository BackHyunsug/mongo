from pymongo import MongoClient 

client = MongoClient("mongodb://test:1234@127.0.0.1:27017/")

#use mydb 
db = client.mydb

db.member.insert({'member_id':'test6'})
rows = db.member.find()
#list of dict 
print(rows)
for row in rows:
    print(row)