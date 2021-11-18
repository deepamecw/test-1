class user:
    course = 'python'
o = user()
print(o.__dict__)
print(o.course)
o.course = 'java'
print(o.__dict__)
print(user.__dict__)
o1 =user()
print(o1.__dict__)