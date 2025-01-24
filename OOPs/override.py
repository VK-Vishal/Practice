class A:
    def __init__(self):
        self.name="hello"
    def met(self):
        print("this is parent")
        print(self.name)
    def met1(self):
        print("this is from parent")
class B(A):
    def met(self):
        print("this is child")  
        super().met()
        super().met1() 
x=B()
x.met()    