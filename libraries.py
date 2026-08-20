import random                 # Importing the random library

# () - parantheses for the function
# [] - list
# "heads" - strings
# stored in a variable(coin)
coin = random.choice(["heads", "tails"])          #  Want to toss a coin
print(coin)


from random import choice
coin = choice(["heads", "tails"])
print(coin)



# pick a number betweeb 1 - 10
from random import randint
num = randint(1, 10)
print(num)



# takes a list of values and shuffles them
import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


 # STATISTICS
import statistics
print(statistics.mean([100, 90]))


# ============ Command line arguments =================
# sys - module

import sys 
try:
    print("hello my name is", sys.argv[1])              # sys.argv[0] stores file name
except IndexError:
    print("too few arguments")



import sys
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else: 
    print("hello, my name is ", sys.argv[1])




import sys 
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
print("hello, my name is", sys.argv[1])



# --------------- MATH - THE CALCULATOR LIBRARY -------------------
import math

math.sqrt(66)
math.pi
math.floor(4.8)             # round down
math.ceil(4.3)               # round up
math.pow(3,4)

