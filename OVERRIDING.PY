class employee:
    def workinghours(self):
        self.hours = 50

    def printhours(self):
        print("Total hours: ",self.hours)
class trainee(employee):
    def workinghours(self):
        self.hours = 60
    def resethours(self):
        super().workinghours()

employee = employee()
employee.workinghours()
employee.printhours()

trainee = trainee()
trainee.workinghours()
trainee.printhours()
trainee.resethours()
trainee.printhours()
