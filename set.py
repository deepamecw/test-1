

"""
names = {'anu', 'shan', 'don','helen'}
print(names)
for name in names:
    print(name)
names.add("pup")
print(names)
a = {"sree","rich","peep"}
names.update(a)
print(names)
names.remove("shan")
print(names)
names.discard("shan")
print(names)
names.pop()
print(names)
names.clear()
print(names)

a = {1, 2, 3, 4, 5}
b = {'e','r','d','f','g'}
c =a.union(b)
print(c)
a.update(b)
print(a)
"""
a = {5,6,7}
b = {5,6,7 }
c = a.difference_update
print(c)
c = a.issuperset(b)
print(c)
c = a.issubset(b)
print(c)