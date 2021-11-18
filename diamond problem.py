class A:
    def display(self):
        print("I am the display of A")
class B(A):
        pass
class C(A):
        pass
class D(C,B):
        pass
o = D()
o.display()