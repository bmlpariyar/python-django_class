#========Control statemnts ==============

list = ["Ram", "Hari", "Shyam", "Gopal", "Sita", "Gita"]

for name in list:
    print(name)
    

while True:
    name = input("What is your name:")
    if name == "Ram":
        continue
        print("Hello world")
    if name == "Hari":
        break
    if name == "Shyam":
        pass
        print("Hello world")
    else:
        print(f"{name} is not in list")
        break



day = input("Enter day: ")

match day:
    case "Sunday":
        print("Happy Holiday!!")
    case "Monday":
        print("Work day")
    case _:
        print("Inalid value")




for i in range(1,11, 3):
    print(i)




books = []

while True:
    print("Welcome user")
    print("1)Add Books\n2)Display Book\n3)Delete Book\n4)Exit")
    
    choice = int(input("Enter your choice(1,2,3,4): "))
    
    if choice == 4:
        break


#Functions and Error Handling
def greet(name=None):
    if name:    
        print(f"Hello, {name}")
    else:
        print("Hello, guest")
    
greet("Ram")

def calculate_percentage(value, percent):
    result = value * (percent/100)
    amout_after_percentage = value - result
    return result, amout_after_percentage


def value(*args):
    return sum(args)

def value_next(**kwargs):    
    for key, value in kwargs.items():
        if value == None:
            continue
        print(f"{key}: {value}")
        

print(value_next(name="Bimal", age=25, job="student"))

print(value(2,5,6))

percent_value, value_after_percentage = calculate_percentage(50, 20)
print(calculate_percentage(50, 20))



# ============+Error Handling=====================

numbers = [1,2,3,4,5]

print(numbers[10])
print("Hello world")

try:
    print(numbers[10])
    print(50/0)
except IndexError as e:
    print("==========================")
    print(f"Error: {e}")
except Exception as e:
    print("==========================")
    print(f"Error: {e}")
else:
    print("==========================")
    print("Success: Viewing is possible")
finally:
    print("==========================")
    print("Finally: Shown the error and the code block is finished")
print("==========================")
print("Outside Block: Hello world")






