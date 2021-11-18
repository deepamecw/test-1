class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printdetails(self):
        print("Name: ",self.name,"Age: ",self.age)
    @staticmethod
    def welcome():
        print("WELCOME TO THE COLLEGE")
S = student("DEEPA PRADEESH",30)
S.printdetails()
S.welcome()
S2 = student("PRADEESH",35)
S2.printdetails()
S2.welcome()