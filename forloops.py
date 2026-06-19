#--------------------------------------FOR LOOPS-----------------------------------------
# for iterating over a sequence


#print each fruit in fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)



# Strings are itreeable objects, they contain a sequence of characters
for x in "banana":
    print(x)



#----------------------------Break Statement-----------------------------
# we can stop the loop before it has looped through all the items
# Exit the loop when x is banana
fruits = ["tropical", "papaya", "leeche" ]
for x in fruits:
    print(x)
    if x == "papaya":
        break



# break comes before print

flowers = ["roses", "jasmine", "lilies"]
for f in flowers:
    if f == "jasmine":
        break
    print(f)




#--------------------------Continue Statement----------------------------
# To stop the current iteration of the loop
# do not print bentley

cars = ["bughatti", "bentley", "audi"]
for c in cars:
    if c == "bentley":
        continue
    print(c)





#---------------------------THe Range Function------------------------
# to loop yhrough a set of code for a specified number of times,it is used
# returns sequence of number starting from 0 by default
# and increments by 1 by default
# ends at a specifed number


for x in range(7):
    print(x)




# adding a parameter (values from 2 to 5; 6 is excluded)

for x in range(2, 6):
    print(x)



# range function increments the sequence by 1 , 
# it is also possible to specify the increment value
# by adding a third parameter
# 2 + 4 = 6,
# 6 + 4 = 10....

for x in range(2, 18, 4):
    print(x)





# ---------------------Else in for Loop----------------------
# print all numbers form 0 to 5, 
# and print a message when the loop has ended

for x in range(6):
    print(x)
else:
    print("finally fifnshed")
    
    
    
    
#---------------------Nested Loop-----------------------------
# inner loop will be executed one time for each iteration
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for b in fruits:
        print(a,b)



        


kids = ["aman", "marium", "khadija", "nirmal", "ashal", "naimal"]