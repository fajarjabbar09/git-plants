#-----------------------------------------T U P L E S--------------------------------------------------
# are ordered an unchangeable ,allows duplicate values
mytuple = ("printer", "laptop", "mouse")
print(mytuple)


# Tuple Length
print(len(mytuple))


# Tuple with one item(add a comma at the end)
tupleone = ("three" ,)
print(type(tupleone))


# NOt a Tuple
tupletwo = ("two") 
print(type(tupletwo)) #just a string


# ----------------------------Tuple Constructor
class2 =tuple(("abieshi","John","stephan","Josh"))
print(class2)


#-------------------------( ACCESS TUPLE ITEMS )-------------------------
room = ("curtains","wardrobe","chair","bed","table")
print(room[1])


print(room[-2])


# range of indexes
makeup = ("primer","foundation","concealor","blush","eyeshadow","marcara","eyeliner")
print(makeup[2:5])


print(makeup[:4])
print(makeup[2:])


# Check if item exists
skincare = ("moisturizer","sunscreen","eyecream","toner")
if "niacinamide" in skincare:
    print("yes, niacinamide is in the skincare tuple")
else:
    print("not present")


#----------------------( UPDATE TUPLE )----------------------------
# CHANGE THE TUPLE INTO A LIST TO BE ABLE TO CHANGE IT 
Skin = list(skincare)
Skin[1] = "base"
skincare = tuple(Skin)                 # converting the list back to tuple
print(skincare)



# --------------------------ADD ITEMS
# CHANGING THE TUPE INTO LIST 
Princesses = ("cinderella", "belle", "snow white","arora")
prin = list(Princesses)
prin.append("rapunzel")
Princesses = tuple(prin)
print(Princesses)


# ADD TUPLE TO A TUPLE
fairies = ("thumbelina", "tinkerbell")
Princesses += fairies
print(Princesses)


#--------------------------REMOVE ITEM FROM THE TUPLE
characters = ("Matilda","Pinnochio","Dumbo","Maleficant")
chrt = list(characters)
chrt.remove("Dumbo")
characters = tuple(chrt)
print(characters)


# -----------------------------( UNPACK TUPLES )-----------------------------
# ASSIGNING VALUES TO A TUPLE IS PACKING
PRINCESS = ("Tinkerbell","Aurora","belle")
(green, pink, yellow) = PRINCESS
print(pink)




