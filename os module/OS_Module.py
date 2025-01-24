#The os module in Python provides a way to interact with the operating system in a
# platform-independent manner. It allows you to perform various system-level tasks like
# file handling, directory management, environment variables, process management, and more.

import os
'''


print(os.getcwd()) #it will print the current working directory
os.mkdir('createdbyos')  # Creates a new directory
#os.chdir('/path/to/directory') it will change the working directory
#os.makedirs('parent_dir/child_dir')  # Creates nested directories
#os.rmdir('directory')  # Deletes an empty directory
#os.removedirs('parent_dir/child_dir')  # Deletes nested directories
#os.path.exists('file.txt')  # Returns True if file or directory exists
#os.rename('old_file.txt', 'new_file.txt')
#os.remove('file.txt')
#print(os.path.abspath('file.txt'))  # Returns the full path of a file
#print(os.getenv('PATH'))  # Fetches the PATH variable
#os.environ['MY_VARIABLE'] = 'some_value'
for file_name in os.listdir():  # Lists all files in the current directory
    print(file_name)


#checjing and creating directory
if not os.path.exists('createdbyos'):
    os.mkdir('createdbyos')
    print('Directory created')
else:
    print('Directory already exists')'''
    
files=os.listdir()
print(files)