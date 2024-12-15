
#String methods and Data structures

name = "Bimal pariyar is in class"
print(name.upper())
print(name.lower()) 
print(name.capitalize())
print(name.title())
print(name.count('i'))
print(name.index("pariyar"))
name_list = name.split()
print(name_list)

string = "       test          "

print("test".join(name_list))
print(name.replace("Bimal", "Ram"))
print(string)
print(string.strip())


filename = "python_clas.py"
filename2 = "IMG_25323.jpg"

print(filename.endswith(".py"))
print(filename2.startswith("IMG"))



list = ["Ram", "Hari", "Bimal", "Gopal", 25, 58, 52.55, True, None]
print(list)
print(list[1])
list[0] = "Krishna"
print(list)

list.append("Gita")
print(list)
list.insert(1, 2000)
print(list)
list.remove("Gopal")
print(list)



list.reverse()
print(list)

number_list = [5,5,8,6,2,5,5]
print(sum(number_list))
number_list.sort()
print(number_list)


tuple = ("BImal", 25, "Pariyar", True)
print(tuple)
print(tuple[0])
# tuple[0] = "Hari"
# print(tuple)

name_tuple = ("Bimal", "Pariyar")
first_name, last_name = name_tuple

print(first_name)
print(last_name)

set1 = {5,5,6,8,5,1,1,5,2,5,4,8,5,5,5,5,7,4,4,1,4}
set2 = {5,6,5,8,7,5,}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

print(set1.union(set2))


dictonary = {"name": "Bimal", "age": 25, "name": "Ram"}
print(dictonary["name"])

dictonary["job" ] = "Developer"
print(dictonary)

