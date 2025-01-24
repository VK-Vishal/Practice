#Positional Arguments:These are the most common type of arguments. The values passed to the function are assigned to the corresponding parameters based on their position in the function call.
#Keyword Arguments:In keyword arguments, you specify the parameter name and the value explicitly in the function call. This allows you to pass arguments in any order.
# Default Arguments: These are parameters that have a default value. If a value is provided for the argument in the function call, that value is used. Otherwise, the default value is used.
#Variable-Length Arguments: These are used when you don’t know in advance how many arguments will be passed to the function. Python provides two types of variable-length arguments
# Keyword-Only Arguments:These are arguments that must be passed as keyword arguments. They are specified after a * in the function definition.

def avg(a=9,b=5):
    print("average:",(a+b)/2)
avg()#default arguments
avg(1)#default arguments
avg(b=3)#default arguments
avg(6,4)#required arguments
avg(b=6,a=4)#key word arguments
def ave(*number):#it takes numbers as tuple
    #This allows the function to accept any number of keyword arguments as a dictionary.

    sum=0
    for i in number:
        sum+=i
    print("Average:",sum/len(number))
ave(8,3,2,5)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person = {"name": "Alice", "age": 25, "city": "New York"}
print_info(**person)
def square(a):
    return a*a
print("square of 6 is:",square(6))
