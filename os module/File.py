#default mode is read mode




'''
1. Opening a File
Syntax: open(filename, mode)
File modes:
'r': Read (default)
'w': Write (overwrite or create new)
'a': Append (add data at the end)
'b': Binary mode (e.g., 'rb' for reading binary)
'x': Exclusive creation (fails if the file exists)


2. Reading from Files
read(): Reads the entire file.
python
Copy code
content = file.read()
readline(): Reads one line at a time.
python
Copy code
line = file.readline()
readlines(): Reads all lines into a list.
python
Copy code
lines = file.readlines()


3. Writing to Files
write(): Writes a string to the file.
python
Copy code
file.write("Hello!")
writelines(): Writes multiple strings (from a list).
python
Copy code
file.writelines(["Line 1\n", "Line 2\n"])


4. Closing the File
Always close a file after use:
python
Copy code
file.close()
Alternatively, use a with statement to automatically close the file:
python
Copy code
with open('file.txt', 'r') as file:
    content = file.read()
    
    
    
5. File Checking & Manipulation Functions
Check if a file exists:
python
Copy code
import os
os.path.exists('file.txt')
Rename a file:
python
Copy code
os.rename('old_name.txt', 'new_name.txt')
Delete a file:
python
Copy code
os.remove('file.txt')



6. Error Handling
Handle potential errors (e.g., file not found, permission errors) using try/except blocks:

python
Copy code
try:
    file = open('file.txt', 'r')
except FileNotFoundError:
    print("File not found!")
    
    
7. File Cursor
seek(): Moves the cursor to a specified position.
python
Copy code
file.seek(0)  # Move to the start
tell(): Returns the current cursor position.
python
Copy code
position = file.tell()
Key Operations Recap
Write: write(), writelines()
Read: read(), readline(), readlines()
Manage: seek(), tell(), os.rename(), os.remove()


'''




#write will overwrite the current content from the file
#append will add the new content to the file
import os
#f=open("import_in_python","r")
#c=f.read()
#print(c)
#f.close()
c="hello"
if os.path.exists("file_by_creation.txt"):
    os.remove("file_by_creation.txt")
else:
    f2=open("file_by_creation.txt","w")
    f2.write(c)
    f2.close()
    print(f2)

with open("import_in_python","r") as f4:
    c=f4.read()
    print(c)
    
    

