#*args is used to pass variable number of arguments to a function
def sum(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("sum of the numbers is:",sum)
sum(1,2,3,4,4)   #this data will be passed as tuple    

#**kwargs is used to pass variable number of keyword arguments to a function

def practice(a,*num):
    print("a:",a)
    print("numbers:",num)
    
practice("vishal",1,2,3,4,5,)  

def show(**kwargs):
    print("keargs",kwargs)
    for i,j in kwargs.items():
        print(i,j)

show(name="vishal",age=23,city="del")

def shows(*args,**kwargs):
    print(args)
    print(kwargs)
    
shows(1,2,3,4,5,one="one",two="two",three="three")