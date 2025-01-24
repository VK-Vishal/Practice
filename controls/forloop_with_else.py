#>>>else block will only execute when for loop is executed successfully

#we can use for loop with else
for i in []:
    print(i)
else:
    print("else of loop")

for i in range(5):
    print(i)
    i=i+1#if u removes this statement it will execute the else block also
    if i==3:
        break
else:
    print("out of loop")
    
#using a while loop
i=0
while(i<7):
    print(i)
    i=i+1
else:
    print("not loop")
    
#loop formating
for i in range(5):
    print("iteration number {} in loop".format(i+1))
else:
    print("else block in loop")