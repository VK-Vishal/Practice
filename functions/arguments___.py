def sum(*numbers):
    c=0
    for i in numbers:
        c+=int(i)
    print("sum of the numbers:",c)
l=str(input("enter the numbers by spaces"))
sum(*l.split())
sum(1,2,2,3,4,5,6,7,8,67,54,45,342)