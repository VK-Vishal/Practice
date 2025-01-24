s1={1,2,3,4}
s2={3,4,5,6,7}
print("union",s1.union(s2))
print("inersection",s1.intersection(s2))
print(s1)
s1.update(s2)#now the s1 one is updated with the values of s2
print(s1)
#similarly interseection update
s1.intersection_update(s2)#here it will update s1 with the insersection with s2
print("after inersectionn update",s1)
#difference and difference update
d1={1,2,3,4,5}
d2={4,5,6,7,8,9,0}
print("finding differnce",d1.difference(d2))#d1-d2
print(d1)
d1.difference_update(d2)
print("after differnece update",d1)

#disjoint() method it checks wheather the elemnets of one set are present in another set
#if present returns false else not presnet return true
#there should be no intersection between them
dis={0,"o"}
dis1={1,2,3,7}
dis2={1,2,3,4,5}
print("checking the disjoint",dis1.isdisjoint(dis2))#it returns false because the 1st set is present in second set
print("checking the oppsite ",dis.isdisjoint(dis1))#it returns true becouse no disjoint

#isuperset
sup={"o",6}
sup1={1,2,3}
sup2={1,2,3,4,5}
print("checking for superset",sup2.issuperset(sup1))#it returns true becouse sup2 have the sup1 value
print("checking for not superset",sup.issuperset(sup1))#it reurns false because sup is not superset of sup1 
print("checking for subset",sup1.issubset(sup2))#true becaus sup1 is subste sup2


#for adding and deleting element 
a={2,3,4}
a.add(5)#adds element in the last
print(a)
a.remove(3)
#a.remove(6) it gives error
a.discard(8)
#to remove and discard the elements 
#here remove raise and error but discard doesnt remove the elemnet
print(a)#it removes the 3 from 

#to remove the last element of the set but we dont know which element is popped becaouse set is unordered
x={5,6,7}
x.pop()
print(x)

#is a key word which del the entire set
del x
#it shows error because x is deleted print(x)

#clear is used to clear the all elements of the set with out deleting the set
y={5,4,6,7}
print(y)
if 4 in y:
    print("present")
y.clear()
print(y)







