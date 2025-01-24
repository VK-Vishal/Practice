a=6
b=7
print(7/6)
print(round(7/6,4))
#Round is a function which takes the number and the number of decimal places to round it to.
#and the default values of decimal is 0
#syntax :round(number,decimal)

#special case:
#round(6.5) will give 6
#round(7.5) will give 8

#>>> here it will round off to the nearest even number

print(round(674,-1)) #round off to the nearest 10
print(round(665,-1))#round off to the nearest 10
print(round(675,-1))#round off to the nearest 10s


#for -2

print(round(674,-2))
print(round(674,-3))
print(round(674,-4))

#here negative will round off to the nearest 10,100,1000,10000