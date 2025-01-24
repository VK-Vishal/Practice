#string is immutable
#string methods operate on string and give the new string
a="HelLo"
print(a.upper())
print(a.lower())
print(a.rstrip("o"))
print(a.replace("l","o"))
b="hello bro how Are yoU"
print(b.split(" "))#it converts atring into list
print(b.capitalize())#it coverts the first charecter to upper and rest to small
print(b.center(40))#it gives moves the string to the center
print(b.count("o"))#it well give the number counting of the charecter in the string
print(b.endswith("oU"))#checks the ending of the string
print(b.startswith("he"))#checks the starting of the strig
print(b.find("Ar"))#find the charecter and returns its 1st index
#if u didnt find it will return -1
print(a.isalnum())#checks the string is alphanumeric
print(a.isalpha())#checks the string is alphabetic
print(a.isnumeric())#checks it numeric
print(a.islower())#checcks its lower case
print(b.isprintable())#checks if its printable
print(b.isspace())#checks for the spaces
print(a.istitle())#returns true is the 1st charecter is only capital
print(a.swapcase())#converts lover to uper and vice versa
print(b.title())#marks the 1st letter of the word capital
