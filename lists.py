# CREATE A LIST 
fruits = ["apple", "kiwi", "banana","grapes", "leeche", "orange"]
print(fruits)


# ACCESS ELEMENTS
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])


# ADD AN ITEM TO FRUITS
fruits.append("mango")
print(fruits)
print("\n")


# REMOVE AN ITEM
fruits.remove("apple")
print(fruits)


# LENGTH OF LIST
numbers = [1, 2, 3, 4, 5 ,6]
print(len(numbers))


# LOOP THROUGH A LIST
colors = ["red" ,"yellow", "green"]
for color in colors:
    print(color)


#SUM OF LIST
Nums = [5, 10, 15, 20]
print(sum(Nums))   


# FIND LARGEST NUMBER
NUMS = [3, 7, 2, 8, 5]
print(max(NUMS))


#CHECK MEMBERSHIP 
if "apple" in fruits:
    print("Found")
else:
    print("Not Found")


# REVERSE A LIST
Num = [1, 2, 3, 4]
Num.reverse()
print(Num)


# COUNT EVEN NUMBERS
Numbers = [1,2 ,4, 7, 8 ,10]
count = 0
for number in Numbers:
    if number % 2 == 0:
        count += 1
print(count)


# CHANGE ITEM VALUE
Cars = ["Bughatti", "mercedes", "Mustang", "Bentley"," Ferarri"]
Cars[1] = "Mercedes" #refered to the index number(change the second item)
print(Cars)


# CHANGE A RANGE OF ITEM VALUES
Cars[1:2] = ["Rolls Royce", "BMW"]   #change the second value by replacing it with two new values 
print(Cars)


#INSERT A NEW ITEM WITH REPLACING ANY EXISTING ONES
Cars.insert(2,"Mercedes")       # inserting at a specific index
print(Cars)


#ADDING ITEM AT THE END OF THE LIST
fruits.append("cherry")
print(fruits)


# EXTEND LIST
tropical =["pineapple","papaya"]  
# to append elements from another list to the current list
fruits.extend(tropical)
print(fruits)


# REMOVE SPECIFIED INDEX
fruits.pop(4)
print(fruits)


# REMOVE AN ITEM AT A SPECIFIED INDEX USING DEL KEYWORD
del fruits[-1]
print(fruits) 


# CLEAR THE LIST
fruits.clear()
print(fruits)


# LOOP THROUGH A LIST
friends = ["Arina", "Sibgha", "Kainat", "Alisha"]
for f in friends:
    print(f)


# LOOP THROUGH THE INDEX NUMBERS
for f in range(len(friends)):
    print(friends[f])


#USING A WHILE LOOP
Jewellery = ["rings", "Bracelets", "Necklace"]
k = 0
while k < len(Jewellery):
    print(Jewellery[k])
    k = k + 1


# LOOPING USING LIST COMPREHENSION
[print(d) for d in Jewellery]


#---------------------------------LIST COMPREHENSION--------------------------------------
Apparel = ["scarfs","sweater","pants","co-ord sets"]
newclothes = [x for x in Apparel if "a" in x]
print(newclothes)


toys = ["bear","cars","dinosaurs","dolls","dollhouse"]
newlist = [t for t in toys if t != "dinosaurs"]
print(newlist)


# creating an iterable
newlist = [ t for t in range(10)]
print(newlist)


# with a condition
newlist = [t for t in range(10) if t < 5]
print(newlist)


newclothes = [x.upper() for x in Apparel]
print(newclothes)


newfriends = ["hello" for f in friends]
print(newfriends)


# keep it in newfruits if it is not a banana if it is a banana replace with orange
Fruits = ["apple","banana", "kiwi","blueberries","raspberry","blackcurrant"]
newfruits = [d if d != "banana" else "orange" for d in Fruits]
print(newfruits)


#---------------------------SORT LISTS-------------------------------
# Sort alphabetically
harrypotter = ["Magicwand","invisiblecloak","Dobby","Hagrid","Broom"]
harrypotter.sort()
print(harrypotter)


# Sort in Descending order
harrypotter.sort(reverse = True)
print(harrypotter)


# Customize Sort Function
def myfunc(n):         # Sort the list based on how close is the number is to 50
    return abs(n - 50)
thislist = [100, 50, 39, 22, 87]
thislist.sort(key = myfunc)       #Before sorting, run each item through the function and sort using those results
print(thislist)


#-------------------CASE SENSITIVE SORT
harrypotter.sort()
print(harrypotter)


# PERFORM A CASE INSENSITIVE SORT OF THE LIST (bcz capital letters are being sorted before lower case letters)
harrypotter.sort(key = str.lower)     # use str.lower as a key function
print(harrypotter)


# REVERSE ORDER OF THE LIST (regardless of the alphabet)
Phones = ["Iphone","Samsung","Huawei","Tecno","Redme","Nexus"]
Phones.reverse()
print(Phones)


#----------------------------------COPY LISTS----------------------------------
Essentials = ["Lotion","Brush","Towel","Perfume","Hairties"]
Essentials = Essentials.copy()
print(Essentials)


# OR (using the list() method)

Essentials = list(Essentials)
print(Essentials)


# OR (use a slice operator to copy a list)
Essentials = Essentials[:]
print(Essentials)


#----------------------------------JOIN LISTS-------------------------------

# concatenate
List1 = ["a", "b", "c"]
List2 = [1, 2, 3]
list3 = List1 + List2
print(list3)


# Append list2 into list1
for g in List2:
    List1.append(g)
print(List1)


# Extend to add list2 at the end of list1
List1.extend(List2)
print(List1)