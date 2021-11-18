class student:
    def __init__(self,total) :
        self._total = total
    def average(self):
        return self._total/5.0
    def getter(self):
        return self._total
    def setter(self,t):
        if t < 0 or t > 500:
            print("invalid data")
        else:
            self._total=t     
    total = property(getter,setter)
s = student(200)
print(s.total)
print(s.average())
s.total = 501
print(s.total)
print(s.average())
