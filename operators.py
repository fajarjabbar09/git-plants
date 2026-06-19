print(10 + 6)
# ------------------------------ARITHEMATIC OPERATORS-------------------------------------
x = int(10)
y = int(8)
#addition
print(x + y)
#subtraction
print(x - y)
#multiplication
print(x * y)
#division (returns a float)
print(x / y)
#floor division (returns integer)
print(x // y)
#modulus
print(x % y)
#exponentiation
print(x ** y) #same as 10*10*10


sum1 = 100 + 30
sum2 = sum1 + 80
sum3 = sum1 + sum2
print(sum1)
print(sum2)
print(sum3)

#---------------------ASSIGNMENT OPERATOR------------------------------------
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x %= y
print(x)
x //= y
print(x)
x **= y
print(x)
x &= y
print(x)
x |= y
print(x)


#-----------------WALRUS OPERATOR
numbers = [1, 2, 3, 4, 5]
if (count :=len(numbers)) > 4:
    print(f"List has {count} elements\n")
#Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
 print("Even")
else: 
 print("Odd")


# CHECK WHICH IS GREATER
i = int(input("Enter first number: "))
o = int(input("Enter second number: "))
print("i > o", i > o)
print("i == o", i ==o)


#AGE ELIGIBILITY TEST 
Age = int(input("Enter your age: "))
if Age >= 18:
  print("Eligible to vote")
else:
  print("Not eligible to vote")



#CHECK RANGE
op = int(input("Enter a number: "))
if 10 <= op <= 50:
  print("Within range")
else:
  print("Out of range")


# COMPOUND BALANCE
balance = 1000
balance += 500   
balance *= 1.50
print("Final Balance: ",balance)


# Login check
register_username = input("Enter username: ")
register_password = input("Enter password: ")
username = input("Enter Username: ")
password = input("Enter password: ")
if username == register_username and password == register_password:
 print("Login Successful")
else:
 print("Login Failed")



#---------------------------------COMPARISON OPERATOR---------------------------------------
A = 200
B = 70
print(A == B)
print(A != B)
print(A > B)
print(A < B)
print(A >= B)
print(A <= B)
# chaining comparison operators
u = 40 
print( 12 < u < 20)
print( 12 < u and u < 20)
print("\n")
#----------------------------LOGICAL OPERATORS (and, or and not)--------------------------------------
print(A > 0 and A < 430)
print(A < 8 or A > 30)
print(not(A > 3 and A < 50))

#-----------LOGICAL OPERATOR (Exercises)
#even and positive check
num3 = int(input("Enter a number: "))
if num3 > 0 and num3 % 2 == 0:
  print("Positive and Even ") 
else:
  print("Neither positive nor Even")


#Marks check
marks = int(input("Enter marks: "))
bonus =input("Bonus(yes/no): ")
if marks >= 50 or bonus =="yes":
  print("passed")
else:
  print("failed")


# Age discount
age = int(input("Enter age: "))
if age < 12 or age > 60:
  print("discount for you")
else:
  print("No discount")


#LEAP YEAR 
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print("It's a leap year")
else:
  print("Not a leap year")


#USERNAME CONDITION CHECK(lenght of username longer than 5 characters and does not equal admin)
user_name = input("Enter username: ")
if len(user_name) > 5 and user_name != "admin":
 print("Username Valid")
else:
 print("Invalid Username")
   

#CHECK IF DIVISIBLE BY 3 AND 5 OR 7
key = int(input("Enter number : "))
if (key % 3 == 0 and key % 5 == 0) and key % 7 == 0:
  print("Condition sstisfied")
else:
  print("Condition not satisfied")

#GRADE CALCULATOR
Marks = int(input("Enter Marks: "))
Attendance = int(input("Enter Attendance: "))
if (Marks >= 80 and Attendance >=75) or Marks >= 90:
  print("Grade A ")
else:
  print("Not Grade A")


#PASSWORD CHECKER
Password = input("Enter Password: ")
if len(Password) >= 8 and ("@" in Password or "#" in Password):
 print("Password is Valid")
else:
  print("Password is not Valid")


#-------------------------------------IDENTITY OPERATORS--------------------------------------
xi = 10
si = 10
print(xi is si) 


go = [1,2,2,3,3]
up = [1,2,2,3,3]
print(go is up)
print(go == up)


ad =[2,3]
bc = ad
print(ad is bc)


aw = "hello"
ew = "hello"
print(aw is ew)


alien = None
print(alien is None)


#------------------------------------MEMBERSHIP OPERATORS--------------------------------------
flowers = ["lilies","roses","plumeras"]
print("lotus" not in flowers)


text = "python\n"
print("py" in text)
print("on" in text)
print("java" in text )

data = [10, 20, 30]
print(40 not in data)
r
#=---------------------------------------BIWISE OPERATORS-------------------------------------------
Park = int(input("Enter first number: "))
Cafe = int(input("Enter second number: "))
print(Park & Cafe)
print(Park | Cafe)
print(Park ^ Cafe)