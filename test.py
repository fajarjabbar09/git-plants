## DONT USE INTERNET UNTIL YOU FINISH THE TEST! ##

# ============================================================
#  Python Practice Test — Fajar Jabbar
#  Topics covered (W3Schools order):
#    Syntax · Output · Comments · Variables · Data Types ·
#    Numbers · Casting · Strings
#
#  Instructions:
#    - Fill in every line marked with:  # YOUR CODE HERE
#    - Do NOT delete any existing code
#    - Run the file when done: python python_test_fajar.py
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — Syntax & Output
# ──────────────────────────────────────────────────────────

# Q1. Print the message:  Hello, I am learning Python!
# YOUR CODE HERE
print("Hello, I am learning Python")

# Q2. Python uses indentation to define blocks.
#     The code below has an indentation error. Fix it.
# if True:
print("Indentation fixed!")  

# Q3. Print three different things on THREE separate lines:
#     your name, your city, and the number 2026
# YOUR CODE HERE
print("Fajar Jabbar")
print("Lahore")
print(2026)

# Q4. Print two words on the SAME line using end="":
#     Output should be:  PythonRocks
# YOUR CODE HERE
print("Python", end ="")
print("Rocks")

# Q5. Use print() with sep argument to produce:  one | two | three
print("one", "two", "three", sep="???")   # <-- replace ??? with correct separator


print("\n--- Section 1: Syntax & Output done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Comments
# ──────────────────────────────────────────────────────────

# Q6. Write a single-line comment that says: This is my practice file
# YOUR CODE HERE (the comment itself is the answer)
# This is my practice file

# Q7. Write a multi-line comment (triple quotes) explaining what Python is used for.
# YOUR CODE HERE
""" Python is used for creating websites and applications """

# Q8. The line below has a bug. Comment it out, then write the correct version.
# prnt("This line is broken")
# YOUR CODE HERE (correct version below)
# This line below has a bug
print("This line is broken")

print("--- Section 2: Comments done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Variables
# ──────────────────────────────────────────────────────────

# Q9. Create variable  name  with your first name as a string.
# YOUR CODE HERE
first_name = "Fajar"

# Q10. Create variable  age  with your age as a number.
# YOUR CODE HERE
age = int(22)

# Q11. Create variable  is_intern  and set it to True.
# YOUR CODE HERE
is_intern ="True"

# Q12. Print all three variables on separate lines.
# YOUR CODE HERE
print(first_name)
print(age)
print(is_intern)

# Q13. Assign THREE variables in ONE line:  x = 10, y = 20, z = 30
# YOUR CODE HERE
x, y, z = (10, 20, 30)

# Q14. Assign the SAME value 0 to three variables a, b, c in one line.
# YOUR CODE HERE
a = b = c = 0

# Q15. Create  color = "red"  and  Color = "blue" , print both.
#      (shows that Python variable names are case-sensitive)
# YOUR CODE HERE
color = "red"
Color = "blue"
print(color)
print(Color)

# Q16. Without running it, what error would this cause?  print(city)
#      Write the error name as a comment.
# YOUR CODE HERE  (example format:  # NameError)
# variable city not present

# Q17. Use  del  to delete variable  y  from Q13, then print "y deleted".
# YOUR CODE HERE
del y
print ("y deleted")

print("--- Section 3: Variables done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Data Types
# ──────────────────────────────────────────────────────────

# Q18. Create one variable of each type and print each with type():
#      str, int, float, bool, list, tuple, dict, set
# YOUR CODE HERE
integer = 23
stri = "Latin"
flo_at = 33.78
_bool = True
List = ["Mushrooms","truffles","Shitake"]
tuple = ("waffles", "pancakes", "donuts")
dict = {"meal": "breakfast",
        "time": "morning",
        "menu" :"spinach omelete"}
set = {"water", "soda", "coffee"}
print(integer)
print(stri)
print(flo_at)
print(_bool)
print(List)
print(tuple)
print(dict)
print(set)
print(type(integer))
print(type(stri))
print(type(flo_at))
print(type(_bool))
print(type(List))
print(type(tuple))
print(type(dict))
print(type(set))

# Q19. Print the type of  3.14
# YOUR CODE HERE
pi = 3.14
print(type(pi))

# Q20. Create  fruits = ["apple", "banana", "mango"]  and print its type.
# YOUR CODE HERE
fruits = ["apple", "banana", "mango"]
print(type(fruits))

# Q21. Store  None  in a variable and print its type.
# YOUR CODE HERE
var = None
print(type(var))

print("--- Section 4: Data Types done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Numbers
# ──────────────────────────────────────────────────────────

# Q22. Create:  p = 20   q = 6
# YOUR CODE HERE
p = 20
q = 6

# Q23. Print results of all 7 arithmetic operations:  + - * / // % **
# YOUR CODE HERE
print(p + q)
print(p - q)
print(p * q)
print(p/q)
print(p//q)
print(p % q)
print(p ** q)

# Q24. Print the type of  100
# YOUR CODE HERE
hun =100
print(type(hun))

# Q25. Print the type of  100.0
# YOUR CODE HERE
hu = 100.0
print(type(hu))

# Q26. Create complex number  c = 3 + 5j  and print it with its type.
# YOUR CODE HERE
comp = 3 + 5j
print(type(comp))

# Q27. Print the absolute value of  -456  using abs()
# YOUR CODE HERE
num = -456
print(abs(num))

# Q28. Use  pow(2, 8)  and print the result.
# YOUR CODE HERE
print(pow(2,8))

# Q29. Import math and:
#      a) Print square root of 144
#      b) Print math.pi rounded to 4 decimal places
import math 


# YOUR CODE HERE

print("--- Section 5: Numbers done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Casting
# ──────────────────────────────────────────────────────────

# Q30. Cast the string "42" to an integer. Print result + its type.
# YOUR CODE HERE
d = int("42")
print(d)
print(type(d))

# Q31. Cast the integer 7 to a float. Print result + its type.
# YOUR CODE HERE
s = float(7)
print(s)
print(type(s))

# Q32. Cast the float 9.99 to an integer. What value do you get? Print it.
# YOUR CODE HERE
n = int(9.99)
print(n)

# Q33. Cast integer 1 to bool and print it.  Then cast 0 to bool and print it.
# YOUR CODE HERE
g = bool(1)
m = bool(0)
print(g)
print(m)
print(type(g))
print(type(m))

# Q34. Fix this line so it prints:  You are 22 years old
user_age = 22
# print("You are " + user_age + " years old")  <-- broken, fix using str() casting
# YOUR CODE HERE (fixed version)
print("You are " + str(user_age) + " years old")

print("--- Section 6: Casting done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 7 — Strings
# ──────────────────────────────────────────────────────────

sentence = "Python is an Amazing Programming Language"

# Q35. Print sentence in ALL UPPERCASE.
# YOUR CODE HERE
print(sentence.upper())

# Q36. Print sentence in all lowercase.
# YOUR CODE HERE
print(sentence.lower())

# Q37. Print the total length (number of characters) of sentence.
# YOUR CODE HERE
print(len(sentence))

# Q38. Print only the FIRST character using indexing.
# YOUR CODE HERE
print(sentence[0])

# Q39. Print only the LAST character using NEGATIVE indexing.
# YOUR CODE HERE
print(sentence[-1])

# Q40. Print characters from index 10 to 20 (slicing).
# YOUR CODE HERE
print(sentence[10 :20])

# Q41. Print sentence REVERSED using slicing  [::-1]
# YOUR CODE HERE
print(sentence[::1])

# Q42. Replace "Amazing" with "Awesome" and print the result.
# YOUR CODE HERE
print(sentence.replace("Amazing","Awesome"))

# Q43. Check if "Python" is IN sentence. Print True or False.
# YOUR CODE HERE
print("Python" in sentence)

# Q44. Check if "Java" is NOT in sentence. Print True or False.
# YOUR CODE HERE
print("Java" not in sentence)

# Q45. Split sentence into a list of words and print the list.
# YOUR CODE HERE
for split in sentence :
 print(split)

# Q46. Strip whitespace from this string and print clean version:
padded = "     Hello Fajar!     "
# YOUR CODE HERE
print(padded.strip())

# Q47. Use lstrip() to remove only LEFT whitespace from padded.
# YOUR CODE HERE
print(padded.lstrip())

# Q48. Count how many times the letter "a" appears in sentence (case-sensitive).
# YOUR CODE HERE
print(sentence.count("a"))

# Q49. Find the INDEX of first occurrence of "Programming" in sentence.
# YOUR CODE HERE
print(sentence.index("Programming"))

# Q50. Use an f-string to print:
#      "My name is <name> and I am <age> years old."
#      (use name and age variables from Section 3)
# YOUR CODE HERE
line = f"My name is {first_name} and I am {age} years old.\n"
print(line)

# Q51. Use .format() to print the same sentence as Q50.
# YOUR CODE HERE
print(line.format())

# Q52. Concatenate first + second and print result:
first = "Hello"
second = "World"
# YOUR CODE HERE  → expected output: HelloWorld
output = first + second
print(output)

# Q53. Print first and second with a space between using concatenation.
# YOUR CODE HERE  → expected output: Hello World
output = first + " " + second
print(output)

# Q54. Repeat "Ha" five times using the * operator.
# YOUR CODE HERE  → expected output: HaHaHaHaHa
repeat = "Ha"

# Q55. Check if sentence STARTS WITH "Python". Print True or False.
# YOUR CODE HERE
print(sentence.startswith("Python"))

# Q56. Check if sentence ENDS WITH "Language". Print True or False.
# YOUR CODE HERE
print(sentence.endswith("Language"))

# Q57. Print sentence in Title Case using title().
# YOUR CODE HERE
print(sentence.title())

# Q58. Use swapcase() on "hELLO wORLD" and print the result.
# YOUR CODE HERE
print(output.swapcase())

# Q59. Use center(60, "-") to center the text "PASS" in a 60-character line.
# YOUR CODE HERE


# Q60. Write a MULTILINE string (triple quotes) with 3 lines of text and print it.
# YOUR CODE HERE

print("--- Section 7: Strings done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project (combines everything)
# ──────────────────────────────────────────────────────────

# Ask the user for:
#   - Their name        (string)
#   - Their birth year  (cast to integer)
#   - Their favourite number (cast to float)
#
# Then print a summary like:
# -----------------------------------------------
#  Name             : Fajar
#  Age in 2026      : 22
#  Favourite number : 7.0
#  Types            : <class 'str'>  <class 'int'>  <class 'float'>
# -----------------------------------------------

# YOUR CODE HERE
Name = str(input("Name :"))
birth_year = int(input("Age in 2026 :"))
favourite_number = float(input("Favourite number:"))
print(Name)
print(birth_year)
print(favourite_number)
print("Types:", type(Name),type(birth_year), type(favourite_number))
#print("Types:" , end="")
#print(type(Name),end="")
#print(type(birth_year),end="")
#print(type(favourite_number))
print("=== All done! Great work Fajar! ===")