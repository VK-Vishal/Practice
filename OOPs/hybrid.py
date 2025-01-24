'''
MRO, or Method Resolution Order, is a crucial concept in Python's object-oriented
programming that determines the order in which methods are searched for in a class 
hierarchy, particularly when multiple inheritance is involved. This ordering is 
essential to ensure that the correct method is invoked when a method is called on 
an instance of a class.


MRO is vital for effectively utilizing inheritance in Python. 
It ensures that methods are resolved predictably and consistently 
across complex hierarchies, especially with multiple inheritance scenarios.
By adhering to the depth-first left-to-right search strategy, Python allows 
developers to manage class behaviors more intuitively

syntax:print(<class name>.__mro__)
       print(<class name>.mro())
       print(<class name>.mro)
       print(<class name>.mro())
       print(<class name>.__mro__[0].__name__)

'''




class A:
    def a(self):
        print("from a")
class B(A):
    print("from b")
class C(A):
    def __init__(self):
        print("from c")
class D(B,C):
    def d(self):
        print("from d and dislay all")
x=D()
x.a()
x.d()
print(D.mro)
print(D.mro())

