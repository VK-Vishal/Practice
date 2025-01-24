 #this functions are used to work with file objects  and their possitions within a file
'''
 ->The seek() function is used to change the current position of the file pointer in a file stream.
 This allows you to move to a specific location in the file for reading or writing.
 WITH BYTES
 
 ->The tell() function returns the current position of the file pointer within the file. 
 This is useful for tracking where you are in the file during read/write operations. 
 
 truncate()-> he tell() function returns the current position of the file pointer within the file. 
 This is useful for tracking where you are in the file during read/write operations.
 
                with open("example.txt", "r+") as f:
                f.read(10)  # Read first 10 bytes
                f.truncate()  # Truncate at current position (10 bytes)

               '''

with open("text.txt","r") as f:
    f.seek(10)
    data=f.read(10)
    print(data)
    print("present position of pointer is:",f.tell())
