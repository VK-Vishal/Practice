#dictionary is a data structure that stores the value in key: value pairs. 
#Values in a dictionary can be of any data type and can be duplicated, 
#whereas keys can’t be repeated and must be immutable.
# create dictionary using { }
d1 = {1: 'one', 2: 'two', 3: 'three'}
print(d1)
print(d1[2])
print(d1.get(1) and d1.get(3))#here if the element is not present it wont give error
# create dictionary using dict() constructor
d2 = dict(a = "1", b = "2", c = "3")
print(d2)
print(d2.keys())
#or
for key in d2.keys():
    print(f"the value corresponding to  {key} is {d2[key]}")
print(d2.values())

print("whole dictionary",d2.items())
for key,value in d2.items():
     print(f"(using lop)the value corresponding to  {key} is {d2[key]}")
d3={"d":4,"e":5,"f":6}
d2.update(d3)
print("updated d2",d2)

#to delete the elements of dictionary we use clear()
d2.clear()
print(d2)

#to remove an element we use pop()
d3.pop("e")
print(d3)

#we use del key word to delete the dictionary
del d2