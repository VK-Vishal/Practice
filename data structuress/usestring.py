a='hel"lo'
print(a)
b='''hello "bro",how are you ,im fine "u"'''
print(b)
c="""hello "bro" i think u are fine ?"""
print(c)
print(a[4])
for char in a:
    print(char)
#string slicing
print(a[0:4])
print(a[2:4])
print(a[:4])#default zero
print(len(a))#length of the string
print(a[0:-1])#it works as length of the string minus negative value here 0:6-1==0:5
print(a[-3:-1])#similarly it works lengt minus the negative value
