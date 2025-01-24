with open("text.txt","r") as f:
    data=f.readline()
    l=len(data)
    print(data,l)

with open("text.txt","a") as f:
    f.writelines("\n added by lines \n 2nd")
    l=len(data)
    print(data,l)

'''
readline= reads a single line
writelines= write data in line wise

'''