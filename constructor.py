class user:
    def __init__(self,name):
        print("call when new instance created")
        self.name = name
    def printall(self):
            print("name: ",self.name)

c =user("DEEPA")
c.printall()
print(c.__dict__)
c1 = user("pradeesh")
c1.printall()
print(c1.__dict__)