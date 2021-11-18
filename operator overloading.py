class operator:
    def __init__(self,a):
        self.a = a
    def __add__(a1,a2):
        return a1.a + a2.a
    def __sub__(a1,a2):
        return a1.a - a2.a
a1 = operator(10)
a2 = operator(20)
print("total: ",(a1 + a2))
print("difference: ",(a1 - a2))