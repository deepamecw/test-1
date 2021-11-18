class student:
    count = 0
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        student.count += 1
    def printdetail(self):
        print("Name: ",self.name, " age is ",self.age)
    @classmethod
    def total(cls):
        return cls.count
D = student("DEEPA",30)
D.printdetail()
w = student("ATUL",8)
w.printdetail()
e = student("anu",13)
e.printdetail()
q = student("pradeesh",40)
q.printdetail()
print("Total admission: ",student.total())