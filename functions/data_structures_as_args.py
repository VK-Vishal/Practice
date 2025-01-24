def show(take):
    print(take)
    
def unpacked(a,b,c,d):
    print(a,b,c,d,sep=" ")
lst=[1,2,4,5]
tup=(1,2,3,4)
s={1,2,3,4}
dict={"one":1,"two":2,"three":3,"four":4}

unpacked(*lst)
unpacked(*tup)
unpacked(*s)
unpacked(*dict.values())
#unpacked(*dict) #TypeError: unpacked() argument after * must be an iterable, not dict
print("-----dictionar------")
def dic_show(d):
   for i,j in d.items():
       print(i,j)
dic_show(dict)
'''show(lst)
show(tup)
show(s)
show(dict)'''