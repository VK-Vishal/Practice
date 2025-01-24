n=int(input("enter the numebr of elements "))
print("enter the key and its value respectively")
d={}
for i in range(n):
    key=input("enter the key")
    value=input("enter th value")
    d[key]=value
print(d)

#for set
print("enter the set elements")
s={int(input()) for i in range(n)}
print(s)

'''#for tuple
print("enter the tuple elements by ,")

t=tuple(n.split(','))
print(t)'''

#for list
print("enter the list elements")
l=[int (input()) for i in range(n)]
print(l)
