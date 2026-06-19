#-------------------------------------IF STATEMENT---------------------------------------------

a = 33
b = 499
if b > a:
    print("b is greater than a")



number = 989
if number > 0:
    print("the number is positive")




# Multiple statements inside an If block. 
# All statements must be indented at the same level
age = 24
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")




# VARIABLES IN CONDITIONS
is_logged_in = True
if is_logged_in:
    print("welcome back!")



#---------------------------------------ELIF STATEMENT-------------------------------------------
# If the previous condition is not True try this statement


A = 33
B = 33
if B > A:
    print("B is greater than A")
elif a == b:
    print("A and B are equal")



# Multiple Elif Statements

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")




age = 25
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")




day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")




#------------------------------------ELSE STATEMENT------------------------------------
# ELSE STATEMENT CATCHES ANYTHING WHUCH ISNT CAUGHT BY THE PRECEDIMG CONDITIONS
 

a = 200
b = 33
if b > a:
    print("b is greater than  a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")




a = 400 
b = 55
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")




number = 7
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")




temperature = 22
if temperature > 30:
    print("Its hot outside")
elif temperature > 20:
    print("Its warm outside")
elif temperature > 10:
    print("Its cool outsode")
else:
    print("Its cold outside")




username = "Emil"
if len(username) > 0:
    print(f"Welcome,{username}!")
else:
    print("Error: Username cannot be empty")




#-------------------------------------SHORTHAND IF-----------------------------------
# IF ONLY ONE STATEMENT TO EXECUTE

C = 5
D = 2 
if C > D: print("C is greater than D")


# conditional expression


c = 2
d = 330
print("c") if c > d else print("d")




a = 10
b = 20
# variable = value_if_true if condition  else value_if_false
bigger = a if a > b else b
print("Bigger is", bigger)




a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")




x = 15
y = 20
max_value = x if x > y else y
print("Maximum vlaue",max_value)




#---------------------------------------LOGICAL OPERATORS--------------------------------------
# Used to combine conditional statements
a = 200
b = 33
c = 566
if a > b and c > a:
    print("Both contitions are True")




a = 220
b = 34
c = 499
if a > b or a > c:
    print("At least one of the conditions are True")



a = 33
b = 200
if not a > b:
    print("a is not greater than b")



# ----Combining Multiple operators----

age = 26
is_student = False
has_disount_code =  True
# The discount applies is :
# the person is under 18 or over 65
# and not a student
# -OR-
# They simply have a discount code 
if (age < 18 or age > 65) and not is_student or has_disount_code:
#   (25 < 18 or 25 > 65)  and not   (False)  or (True)    
#   (false   or  false)   and not  (False)  or (True)
#        (False)       and      (True)   or (True)
#                    (False)    or    (True)
#                            (True)     
   print("Disount applies")



temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities")




username = "Tomy"
password = "secret123"
is_verified = True
if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")




score = 85
if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")




# ----------------------------------------NESTED IF STATEMENTS--------------------------------

x = 41
if x > 10 :
    print("Above ten,")
    if x > 20 :
        print("and also above 20!")
    else:
        print("but not above 20.")



age = 25
has_license = True

if age >= 18:
    if has_license:
     print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")



score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with standing")
        else:
            print("passed with missing assignment")
    else:
        print("pass but low attendance")
else:
    print("Fail")




#---------------------------------PASS STATEMENT--------------------------------
# a Null Operation 

a = 33
b = 200
if b > a:
    pass   



age = 16
if age < 18:
    pass
else:
    print("Access granted")


score = 85
if score > 90:
    pass
print("score processed")


# ---Pass with multiple conditions----
value = -50
if value < 0:
    print("Negative value")
elif value == 0:
    pass
else:
    print("Positive value")




def calculate_discpunt(price):
    pass




