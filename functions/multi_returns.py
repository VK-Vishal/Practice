# The most common approaches are using tuples, lists, dictionaries, 
# or even returning multiple values directly (which Python automatically treats as a tuple)
def mutlti_return(numbers):
    sum=0
    product=1
    for i in range(1,len(numbers)+1):
        sum+=i
        product*=i
    avg=sum/len(numbers)
    return sum,product,avg

result=mutlti_return([1,2,3,4,5])
print("sum:",result[0],"product:",result[1],"average:",result[2],sep="\n")