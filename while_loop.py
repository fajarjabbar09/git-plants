#-------------------------------WHILE LOOPS---------------------------

i =1
while i < 6:
    print(i)
    i += 1



# ----break statement----
# t stop the loop even if the while condition is true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# -----the continue statement------
# to stop the current itreation and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)




#-----Else statement-------
# run a block of code once the condition is no longer true
i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
print("\n")



# Print numbers form 1 to 10
i = 1
while i <= 10:
    i += 1
    print(i)
    
