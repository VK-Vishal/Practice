#two types of functions :built in and user defined
def add(a,b):
    print(a+b)
def great(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(a==b):
        print(a,b,"are equal")
    else:
        print(b,"is greater than",a)
a=int(input("enter a number"))
b=int(input("enter another number"))
add(a,b)#function call
great(a,b)
def lesser(a):#function defination
    pass