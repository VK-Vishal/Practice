marks=[67,78,76,89,98,99,69,56,80]
for index,mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("highest mark!")
#The enumerate() function returns an enumerator object,
# which produces pairs of index and value from the iterable during each iteration.
#iterating with starting index
fruits = ['apple', 'banana', 'cherry']

# Start indexing from 1
for index, value in enumerate(fruits, start=1):
    print(f"Index: {index}, Value: {value}")
    
#ccreating dictionary with enumerate function
names = ['Alice', 'Bob', 'Charlie']

# Create a dictionary using enumerate
name_dict = dict(enumerate(names, start=1))
print(name_dict)


