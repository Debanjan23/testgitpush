import pymongo
client = pymongo.MongoClient("mongodb+srv://root:Skhan87!@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


