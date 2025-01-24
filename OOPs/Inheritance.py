'''

=>Single Inheritance: A child class inherits from a single parent class.

=>Multiple Inheritance: A child class inherits from more than one parent class.

=>Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.

=>Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

=>Hybrid Inheritance: A combination of two or more types of inheritance.

'''

class A:
    def met(self):
        print("this is father")
class B(A):
    def metb(self):
        print("this is child")
b=B()
b.met()
b.metb()