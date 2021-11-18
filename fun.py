"""
def mul():
    a = int(input("enter the value of A: "))
    b = int(input("enter the value of B:" ))
    c = a*b
    print(c)
    return c
c = mul()
print("mul",c)
def div(d,e):
    f = d/e
    return f
x = div(20,10)
print("div",x) 
"""
def class_10(*students):
    print(students)
    for user in (students):
        print(user)

class_10('sara','vel','donu')