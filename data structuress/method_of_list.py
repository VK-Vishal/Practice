#precende of operators:
 # () ,** ,/ ,* ,+ ,- ,&(bitwise operator) ,| ,(==,>,>=,>,<=,!=) , not, and, or
 #--->-------------------->------------------->-------------------->---------->

a=[i for i in range(15)]
b=[16,17]
a.append(15)#add in the end
#a.append(b)
print(a)
a.reverse()
print(a)
c=[3,5,1,5,5,6,4,36,7,9]
c.sort()
d=[3,5,1,5,6,4,36,7,9]
d.sort(reverse=True)
print(c)
print(d)
print(a.index(4))#returns the indea of that number
print(c.count(5))#counts the number of times it appers in list
e=d
e[0]=0
print(d)#it will also make change in the original list
f=d.copy()
f[0]=1
print(d,f)#here new list is changed
f.insert(0,11)
print(f)#inserting element at an index
a.extend(b)#adding the elements of one list to anothe list at the end
print(a+b) 
print(a)