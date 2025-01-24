'''


The slicing syntax sequence[start:stop:step] is used to extract a portion (or "slice") of a sequence (like a list, string, or tuple) based on index positions.

Here's a detailed breakdown of the components:

Key Terms
Index:
Every element in a sequence has an assigned position, starting from 0 for the first element.
For example, in the string "Python", the indices are:
css
Copy code
P  y  t  h  o  n
0  1  2  3  4  5
Negative indices can also be used to count from the end:
css
Copy code
P   y   t   h   o   n
-6 -5 -4 -3 -2 -1
Copy code
Components of sequence[start:stop:step]
start:

The index where slicing begins.
If omitted, it defaults to the first index (0 if step is positive, or -1 if step is negative).
stop:

The index where slicing ends (exclusive). The slice stops before this index.
If omitted, it defaults to the end of the sequence if step is positive, or the start of the sequence if step is negative.
step:

The stride or increment. It determines the gap between the indices to include in the slice.
A positive step moves left to right, while a negative step moves right to left.
Default is 1 if omitted.

'''











#we can change the elemnets in list
# Take space-separated marks as input
marks = input("Enter your marks separated by space: ").split()

# Convert each mark to an integer
marks = list(map(int, marks))

# Calculate the sum and average
total = sum(marks)  # Use a variable name other than `sum`
average = total / len(marks)

# Print the average
print("The average of your marks is", average)
#list can contain hetirogenious data
a=[1,3,3.4,-1,"vishal","k","True",False]
print(a[4])
print(a) or print(a[:]) 
print(a[1:]) or print(a[-2:]) #slicing
print(a[1:6]) or print(a[1:6:3])#jumping
print(a[::])
print(a[-2])#negative indexing means it gives by subtracting (length of array -neagative index) 
#here 8-2=6 it prints True
if "vishal" and "3" in a:
    print("yes")
else:
    print("no")#her no because we are giving number as string
if "vis" in "vishal":
    print("present")
    
#list comprehension
list=[i*i for i in range(10) if i%2==0]
print(list)