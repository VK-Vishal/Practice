a=int(input("eneter a number"))
match a:
    case 0:
        print("number is zero")
    case 1:
        print("number is one")
    case 2:
        print("number is two")
    case _ if a>0:
        print("number is gretaer than 2")
    case _ if a<0:
        print("number is negative")
    case _:
        print("this is default case")

