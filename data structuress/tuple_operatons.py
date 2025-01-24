#1st u have to convert tuple to list and perform operation and then change it into tuple again
a=(1,2,3,4,5,6,3,7,8,9,0)
temp=list(a)
temp.append(2)
print(temp.count(2))#here count will return a vlaue
a=tuple(temp)
print(a)
c=(1,2,3)
d=(4,5,6)
e=c+d#we can add two tuple
print(e)
print(c.index(3))#it gives the index of the elemnet in that list
res=a.index(3,4,8) 
res2=a.index(3,2,8) #1st item takes the value and the the 2nd and 3r are the starting and ending index it between it seraches the index of that elemnent
print(res,res2)
length=len(a)
print(length)