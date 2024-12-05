student = [
    {"name":'Bimal', "age":24, "grades":("A", "A+", "B")},
    {"name":'Ram', "age":25, "grades":("A", "A+", "B")},
    {"name":'Hari', "age":29, "grades":("A", "A+", "B")},
]

print(student[0]["grades"][0])





name = "Bimal"
age = 20
if name == "Bimal":
    if age == 24:
        print("you are old")
    print("Hello ", name)
elif name == "Hari":
    print("Hello somthing")
else:
    print("Hello guest")
    

number = 7

match number:
    case 1:
        print(1)
    case 2: 
        print(2)
    case 5: 
        print(5)
    case _:
        print("Invalid num")
        
        

list = ["Bimmal", "Ram", "Hari"]
print(list)

for i in list:
    print(i)
    
    
    
for num in range(10):
    print("*"*num)
    
num = 5 
i = 1
while i <= num:
    print(i)
    i+=1