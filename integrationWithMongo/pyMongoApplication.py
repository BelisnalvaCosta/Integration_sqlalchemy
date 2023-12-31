import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://mongo:senha@cluster.yoczfda.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

# definição de infor para compor o doc
post = {
    "author": "Ana Paula",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as informações
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(db.posts.find_one())
pprint.pprint(db.posts.find_one())

#bulk inserts
new_posts = [{
            "author": "Ana Paula",
            "text": "Rua Sete de Setembro, 45 - São Paulo",
            "tags": ["00000000911", "post", "insert"],
            "date": datetime.datetime.utcnow(2009, 23, 15, 5)},
            {
            "author": "Roberto Alves",
            "text": "Post from Roberto. New post available",
            "title": "Parabéns, foi efetuado com sucesso!",
            "date": datetime.datetime(2021, 15, 10, 20, 47)}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nRecuperação final")
pprint.pprint(db.posts.find_one({"author": "Roberto"}))

print("\n Documentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)