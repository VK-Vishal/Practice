#tuple is immutable
a=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
b=(1)#its a int ,you have to give comma after the element
c=(1,)
print(type(b),type(c))
#a[0]=2#it csnt be changed
#tuple also have heterrogenious data
d=(1,2,3.4,"k",'t',"kumar")
#similarly negative indexing
print(d[-2])
if 3 in a:
    print("3 is in tuple a")
#similarly we can make slicing
a2=a[1:10:2]
print(a2)