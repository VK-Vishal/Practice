d={1:'one',
   2:'two',
   3:'three'}
print(d)
nes_d={1:'one',
       2:{
           2:'two',
           3:[1,2,3,4,5,6]
       },
       3:{
           4:'foue',
           5:(7,8,9)
       },
       6:'six'
       }
for i,j in nes_d.items():
    print(i,j)
    

#student data:
data={
    "23ucomp001":{
        "name":"adi",
        "age":"19",
        "branch":"cse"
    }
    "23ucomp002":{
        "name":"anay",
        "age":"19",
        "branch":"cse"
    }
    "23ucomp003":{
        "name"="aniket",
        "age"="19",
        "branch"="cse"
    }
    "23ucomp004":{
        "name"="anish",
        "age"="19",
        "branch"="cse"
    }
    
}
print(data)