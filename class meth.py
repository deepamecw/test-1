class student:
    name = "pradeesh"
    age = 35

    def printall():
        print("student name: ",student.name)
        print("Age: ",student.age)
student.printall()
print(student.__dict__)
print(getattr(student,"printall"))
getattr(student,"printall")()
student.__dict__['printall']( )

