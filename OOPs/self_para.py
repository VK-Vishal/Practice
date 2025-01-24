#self parameter is a reference to the current instance of the class. 
# It allows us to access the attributes and methods of the object.
# It binds the attributes with the given arguments.
# The reason you need to use self. is because Python does not use the @ syntax to refer
# to instance attributes.
class Hello:
    def __init__(self,name):
        print("hello",name)
    def hi(self,name,greet):
        print("hi",name,greet)

h1=Hello("vishal")
h1.hi("vishla","good morning")