class A:
    def a(self):
        print("from a")
class B(A):
    def b(self):
        print("from b")
class C(B):
    def c(self):
        print("from c")
x=C()
x.a()
x.b()
x.c()