class A:
    def a(self):
        print("from a")
class B(A):
    print("from b")

class C(A):
    def __init__(self):
        print("from c")
x=C()
y=B()
y.a()