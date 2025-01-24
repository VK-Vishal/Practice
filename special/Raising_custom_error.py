#we can use raise keyword to raise custom error
n=input("enter a numebr")
if(n=='quit'):
    if(n=='quit'):
        print("quitting....")
    
elif n.isdigit():
    n=int(n)
    if(n>0 and n<10):
        raise ValueError("numebr is not valid")
    else:
        print("correct numeber")
else:
    raise TimeoutError("invallid input")