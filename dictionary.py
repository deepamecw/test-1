"""
user = {
    "name": "ram",
    "age" : 25,
    "isMarried" : True
}
print(user)
print(type(user))
print(user["name"])
print(user["age"])
print(user["isMarried"])
print(user.get("name"))
print(user.items())
print(user.keys())
for i in user: 
    print(i, " ",user[i])
user.update({"gender" : "male"})
print(user)
user["age"] = 35
print(user)
user["isMarried"] = False
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
print(user)
"""
users={
"user1": {
    "name": "ram",
    "age" : 25,
    "isMarried" : True
},
"user2": {
    "name": "sam",
    "age" : 35,
    "isMarried" : True

}
}
print(users)
