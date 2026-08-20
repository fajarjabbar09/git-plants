# storing information on your device

# "w" - wrires and rewrites the file 
#name = input("whats your name?: ")
#file = open ("names.txt", "w")
#file.write(name)
#file.close()


# "a" - appends with no spaces between them
#name = input("names: ")
#file = open("names.txt", "a")
# addimg \n for the extra line  
#file.write(f"name{name}\n")
#file.close()



# closing automatically
#with open ("names.txt", "a") as file:
#    file.write(f"{name}\n")




# reading existing file
#with open("names.txt", "r") as file:
#    lines = file.readlines()
# print each line
#for line in lines:
#     print("hello,",line.rstrip() )




# shorter version
#with open ("names.txt", "r") as file:
 #   for line in file:
  #      print("hello,", line.rstrip())


# sorting the names of the members
#names = []        # empty list for names
#with open("names.txt", "r") as file:
 #   for line in file:
  #      names.append(line.rstrip())
#for name in sorted(names):
 #   print(f"hello, {name}")



# storing a  students information
# using a csv file to store dats in the form of column 




# getting access to individual values
#with open("names.csv") as file:
 #   for line in file:
  #      row = line.rstrip().split(",")     
   #     print(f"{row[0]} is in {row[1]}")




# unpacking the values into two variables
students = []               # for sorting the names
with open ("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} in in {house}")
# displaying the sorted names
#for name in sorted(names):
 #   print(name)
 #sorting by students 
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)            # appending the new student to the students list
for student in students:
    print(f"{student['name']} is in {student['house']}")


