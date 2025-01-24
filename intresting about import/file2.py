def hello():
    print("welcome,to the world")
    
print(__name__) #if u run from main file it will print __main__ else if u print from another file it will print file2
if __name__=="__main__":
    hello()
    
