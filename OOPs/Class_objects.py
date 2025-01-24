#A class is a blueprint for creating objects. It defines attributes (variables) and methods (functions) that
# the objects of the class will have.
#A class is defined using the class keyword followed by the class name. The attributes and methods of the 


#An object is an instance of a class. When a class is defined, no memory is allocated for its attributes
# is a real-world entity that you interact with using its attributes and methods.
#An object is created using the class name followed by parentheses. The attributes of the object are set

#object creation or  object instantiation.

#class name shoud be in pascal case ex:AppleBallCat


class details:
    def greet(self,name):
        print("hello:",name)

p1=details()
n=input("enter yout name:")
p1.greet(n)