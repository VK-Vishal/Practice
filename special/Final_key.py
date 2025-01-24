try:
    l=[1,2,3]
    i=int(input("enetr index"))
    print(l[i])
except:
    print("error occured")
finally:
    print("its always executed")

def fun():
    try:
        l=[1,2,3]
        i=int(input("enetr index"))
        print(l[i])
        return 1
    except:
        print("error")
        return 0
    finally:
        print("always executed")
    print("here it wont execute this")
x=fun()
print(x)
    
#the use of finally is to execute that in a function even after ruturning from try and catch
