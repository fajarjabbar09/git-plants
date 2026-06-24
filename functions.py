#=========================== FUNCTION ========================
# ONLY RUNS WHEN IT IS CALLED, AVOIDS CODE REPETITION
# REUSABLE BLOCK OF CODE
# can call a function multiple times

# keyword  function_name(): 
def my_function():
    print("Hello from a function")

# calling a function
my_function()



# ---------------for example---------------
# to convert temperatures from Farenheit to celsius several times in a program 
# you have to write the same calculation code repeatdelu



# keyword function_name (input)
def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5 / 9
print(farenheit_to_celsius(77))
print(farenheit_to_celsius(98))
print(farenheit_to_celsius(39))



def get_greeting():
    return "hello from a function"
message = get_greeting()
print(message)


# if a function does not have return statement it returns None by default
def get_greeting():
    return "hello from the function"
print(get_greeting())


# function definition can not be empty.
#  If you need to create a function placeholder without any codde
# use pass statement


def My_function():
    pass



#=-=-=-=-=-=-=-=-=-=-=-=-=-Function arguements-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# specified after function names
# inside parentheses 
# can add as many arguments as you want
# just seperate them with a comma 


def my_func(fname ):
# concatenation used
    print(fname + " Refsnes")

my_func("Emil")
my_func("abieshie")
my_func("daniel")



# Parameter = variable inside a function
# Argument = actual value passed to the function

def greet(name):
    print("Hello " + name)

greet("Ali")         # "ali" is the argument, arguement gets passed into the parameter




# Multiple Arguments
# Arguments are matched by position

def full_name(first, last):
    print(first + " " + last)
full_name("Fajar", "Jabbar")



# =-=-=-=-=-=-=-=-=-=-=Default Arguments=-=-=-=-=-=-=-=-=-=-=
# they are flexible 
def greet(name = "Guest"):
    print("hello",name)

greet()    # calling without argument


def my_funct(name = "friend"):
    print("hello", name)
my_funct("ALEX")
my_funct("Amelia")
my_funct()
my_funct("Salar")



def power_on(device = "Computer"):
    print(device + " is ON")

power_on()
power_on("Tv")



#=-=-=-=-=-=-=-=-=-=-=-=-=-Keyword argument=-=-=-=-=-=-=-=-=-=-=-=
# arguments can be assigned by specifieying parameter names
# with keyword argument, the order of the argument does not matter

def student(name, age):
  print(name, age)
student(age = 21, name = "fajar") 



def my_farm(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is",name)

my_farm(animal="dog", name= "Woody")



#=-=-=-=-=-=-=-=-=-=-=-=-=Positional Argument=-=-=-=-=-=-=-=-=-
# when you call a function with argument without using keyword
# must be in a correct order

def my_home(society, street):
    print("I have a home in", society)
    print("My home is in", society, "on", street )
my_home("Lakecity", " street no. 12")




# =-=-=-=-==-=-=-=Passing different datatypes=-=-=-=-=-=-=-==-=-=
# Create  a function
def MY_Function(fruits):

    # Go through each fruit in  the list
    for fruits in fruits:

        # Show the fruit
        print(fruits)

# Create a list of fruits
my_fruits = ["apple","kiwi", "cherry"]

# Run the function using the list
# fruits = my_fruits
MY_Function(my_fruits)




# Dictionary as an argument

def my_Function(person):
    print("Name:", person["name"])
    print("Age:",person["age"])
my_person = {"name": "Emil", "age": 25}
my_Function(my_person)




def my_function(x, y):
    return x + y
result = my_function(5, 3)
print(result)



# Returning different data types
def my_perfume():
    return ["miss dior", "crystal noir", "Burberry her"]
perfume = my_perfume()
print(perfume[0])
print(perfume[2])
print(perfume[1])



def my_numbers():
    return(10, 20)
x, y = my_numbers()
print("x:", x)
print("y:", y)


#=-=-=-=-=-==-=-=-=Posiitonal Only Arguments=-=-=-=-=-=-=-=-=-=-
# Everything before / must be positinal only
# / does not allow keyword names for these parameters
def my_fun(name, /):
    print("Hello", name)

my_fun("Emil")



# =-=-=-=-=-=-=-=-=-=-Keyword Only Argument=-=-=-=-=-=-=-=-=-
def my_bags(*, bag):
    print("collection of", bag)
my_bags(bag = "Christian Dior")





# =-=-=-=-Combinig Positional only and Keyword only argument=-=-=-=-=-=
def my_alpha(a ,b ,/ ,* ,c ,d):
    return a + b + c + d
result = my_alpha(5, 10, c = 18, d = 28)
print(result)





#===============---===== args and kwargs ================---=====
# WHEN YOU DONT KNOW HOW MANY NUMBER OF ARGUMENTS WILL BE PASSED INTO YOUR FUNCTION
# THEY ALLOW FUNCTIONS TO ACCEPT A UNKNOWN NUMBER OF ARGUMENTS
# THIS WAY THE FUNCTION WILL RECIEVE A TUPLE OF ARGUMENTS AND CAN ACCESS THE ITEMS ACCORDINGLY

def my_party(*kids):
    print("The yongest child is " + kids[-1])

my_party("Aiman", "Kulsoom", "Laiba", "kareem", "Ayesha", "hasan")



# *Args: Collect extra positional arguments
#can be used in:
# calculator
# shopping cart
# score totals
# printing lists
def my_books(*args):
    print("Type:", type(args))
    print("First Argument:",args[0])
    print("Second Argument:",args[1])
    print("All arguments",args)
my_books("namal", "mein anmol", "peerekamil")



def welcome(greeting, *names):
 for name in names:
     print(greeting, name)
# hello assigned to greetings and rest are collected in names
welcome("hello", "emil", "tobias", "linus")



# function calculates the sum of any number of values
def my_calcu(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_calcu(1, 2, 2, 7))
print(my_calcu(23, 20, 40))
print(my_calcu(5))




def user(**info):
    for key, value in info.items():
        print(key,value)
user(name= "emil", age = 25)



def my_max(*numbers):
    if len(numbers) == 0:     #empty check
        return None
    max_number = numbers[0]  # needs a starting point  for comparison soo get the first item
    for num in numbers:
        if num > max_number:
         max_number = num
    return max_number
print(my_max(23, 34, 82, 63, 20))




# **Kwargs: a dictionary of arguments

def my_names(**kids):
    print("his last name is " + kids["lname"])
my_names(fname = "taha", lname = "jabbar")




def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("all data:", myvar)

my_function(name = "julliete", age = 22, city = "london")



def my_friends(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
my_friends("fajar123", age = 27, city = "oslo", hobby = "painting")




# combining args and kwargs 
def my_library(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("keyword arguments:", kwargs)

my_library("Userinfo", "emil", "tobias", age = 33, city = "oslo")





# UNPACKING LIST WITH ARGS
def add(a, b, c):
    return a+ b + c
nums = [1, 2, 3]
su = add(*nums)
print(su)
# or
print(add(*nums))

# UNPACKING DICTIONARIES WITH KWARGS
def my_client(fname, lname):
    print("hello", fname, lname)
person = {"fname": "amal", "lname":"madam"}
my_client(**person)




#============================ SCOPE ===================================

#=-=-=-=-=-=-=-=-=-=-=-=-=-= LOCAL SCOPE =-=-=-=-=-=-=-=-=-=-=-=-=-=-==
def my_func():
    x = 300
    print(x)
my_func()


#----------------------Function inside Function------------------------
# LOCAL FUNCTION CAN BE ACCESSED FROM A FUNCTION WITHIN A FUNCTION
def myfunc():
    e = 400
    def myinnerfunc():
        print(e)
    myinnerfunc()
my_func()



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-= GLOBAL SCOPE =-=-=-=-=-=-=-=-=-=--=-=-
w = 288
def mywaste():
    print(w)
mywaste()
print(w)


# Same variable name inside and outside of the function is treated as two separate variables, one as globbal scope and one as local scope
s = 100             # Global Scope
def varia():
    s = 229           # Local scope 
    print(s)
varia()
print(s)




# If you need to create a global variable but stuck in a local scope
# GLOBAL keyword can be used to create global variable
def practice():                # defined function
    global p
    p = 66
practice()             # executes and creates a global variable p
print(p) 




# TO CHANGE THE VALUE OF A GLOBAL VARIABLE INSIDE  A FUNCTION REFRE TOO THE VARIBALE USING THE GLOBAL KEYWORD
q = 90
def mymistake():      # writing a  recipe
    global q             
    q = 99
mymistake()              # cooking the dish
print(q)                  # cant get food until you cook it



# =-=-=-=-=-=-=-=-=-=-=-=- NON LOCAL KEYWORD =-=-=-=-=-=-=-=-=-=--=-=-=-=-
# USED TO WORK WITH VARIABLES INSIDE NESTED FUNCTIONS
# NONLOCAL KEYWORD MAKES THE VARIABLE BELONG TO THE OUTER FUNCTION

def myfunc1():
    x = "Jane"
    def myfunc2():    # defined inner function,dont create new local variable
        nonlocal x    # use x from the outer function
        x = "Austin"         # changes the outer x in func1
    myfunc2()
    return x
print(myfunc1())



#=================------------ LEGB RULE ----------=========================
# LOCAL - inside the current function
# ENCLOSING - Inside enclosing funcions(from inner to outer)
# GLOBAL - at the top level of the module
# BUILT-IN - In python's built-in namespace
 



x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global: ", x)




#=========================== DECORATORS ==================================
# LETS YOU ADD EXTRA BEHAVIOUR TO A FUNCTION 
# WITHOUT CHANGING FUNCTIONS CODE
# TAKES ANOTHER FUNCTION AS INPUT AND RETURNS A NEW FUNCTION



# step 1: reads function 
# step 3: function is passed into decorator

def changecase(func):         # changecase(func = my function) 
# step 4: inner function is created (just defined)
    def myinner():                    # call original function("hello sally")
        return func().upper()            #convert it to uppercase
# step 5: decorator returns new function   
    return myinner          # myfunction = myinner
# step 2: reaches decorated function 

@changecase          # python is replacing myinner with myfunction
def myfunction():             
    return "hello sally"

print(myfunction())   # it is now actually myinner



@changecase
def otherfunction():
    return "I am good !"

print(otherfunction())


# Arguments in the decorated function
def changecase(func):
    def inner(x):
        return func(x).upper()
    return inner
@changecase
def myfunct(name):
    return "hello " + name

print(myfunct("john"))




# =-=-=-=-=-=-=-=-=-=-=DECORATORS WITH ARGUMENTS=-=-=-=-=-=-=-=-=-=-=-=-
def changecase(n):
    def changecase(func):
        def Myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a 
        return Myinner
    return changecase

@changecase(1)
def myfunction():
    return "hello linus"
print(myfunction())



def hello(to = "world"):           # def function(parameter = "default"):
    print("hello,", to)     # adding argument


name = input("What's your name? ")
hello(name)          # calling function and passing name variable as an argument






# ======================= LAMBDA FUNCTION ==========================
# ANONYMUS FUNCTION
# lambda arguments : expression
# ne use function
#sort(), map()

x = lambda a : a + 20
print(x(5))



d = lambda b, c : b * c
print(d(3,8))


def myfun(n):
    return lambda a : a * n
mydoubler = myfun(3)
print(mydoubler(18))


def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(6))



# LAMBDA WITH BUILT IN FUNCTIONS
#

# Double all the numbers ina list

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2,numbers))
print(doubled)



numberss = [1,2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x : x % 2 != 0,numbers))
print(odd_numbers)



students = [("Emil",25), ("Tobias", 22), ("Tom", 23)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)


# ================= RECURSION =======================
# Every recursive function must have two parts:
# base case - condition that stops the recursion
# recursive case  - function calling itself with a modified argument

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
countdown(8) 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# =-=-=-=-=-=-=-=-=-=-=- fibonacci sequence =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))