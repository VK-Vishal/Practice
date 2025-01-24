class A:
    def __init__(self):
        print("hello ")
    def a(self):
        print("a from A")
class B:
    def __init__(self):
        print("hi")
    def b(self):
        print("b from B")
class c(A,B):
    def __init__(self):
        print("bye")    
    def c(self):
        print("c from C")
x=c()
x.a()
x.b()
x.c()