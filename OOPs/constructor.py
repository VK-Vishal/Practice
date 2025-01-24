#__init__ method is the constructor in Python, automatically called when a new
# object is created. It initializes the attributes of the class.
# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.

#=>>>>__init__: Special method used for initialization.
#it will directly run the init method when the object is created.

class Hello:
    def __init__(self,name):
        print("hello",name)
h=Hello("antony")