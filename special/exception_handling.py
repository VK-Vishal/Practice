#Error in Python can be of two types i.e. Syntax errors and Exceptions. 
# Errors are problems in a program due to which the program will stop 
# the execution.On the other hand, exceptions are raised when 
# some internal events occur which change the normal flow of the program. 
n=input("eneter a numebr")
try:
    for i in range(1,11):
        print(f"{n}x{i}={int(n)*i}")
except Exception as e:
    print("error",e)
print("important code")

try:
    x=int(input("enter another number"))
    a=[1]
    print(a[x])
except ValueError:
    print("input is not a number")
except IndexError:
    print("inedx out of range")
        

    