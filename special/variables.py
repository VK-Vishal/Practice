#a variable is a named reference used to store data or a value.
a=3
b,c,d=5,6,8
e=f=0
print(a,b,c,d,e,f)
def f():
    c=0
    d=7
    print(a,c,d)
    global f
    f=9
    print(c,f,d)
f()
print(c,f,d)
    