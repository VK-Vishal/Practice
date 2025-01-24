def vow(arr):
    sum=0
    vovels="aeio"
    for i in arr.lower():
        if i in vovels:
            sum+=1
    print("no of vowels is:",sum)
vow("hello world")