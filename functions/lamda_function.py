#************we can pass function as a argument..

def square(fxn,fx,x):
    return fxn(x)+fx(x)


#lambda function is used when you want to define a function in a single line
squares =lambda x: x*x

print("with lamda function:",squares(6))


#syntax : name=lamda arguments: expression

cube= lambda x:x**3

print("sum of sqaure and cube is:",square(cube,squares,10))

print("sum of cubes",square(cube,lambda x:x*x*x,7))

multi=lambda x,y:x*y