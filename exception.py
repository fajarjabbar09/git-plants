while True:     # loop for going on until users give what i want (integer)
    try:
        x = int(input("What's x? "))     # if i get the integer  and No valueerror happens skip the except

    except ValueError:  
        print("x is not an integer")
    else:        
        break           #break out of the loop if you get the integer without error otherwise(it will keep asking for x)
print(f"x is {x}")              # print this after breaking ou
 



# -------------------- OR ----------------------
# thpugh it i not preferrable to add this many line sof code in the (try)
while True:
    try:
        y = int(input("Whats y?"))
        break
    except ValueError:
        print("y is not an integer")

print(f"y is {y}")





# Function
# function whose purpose is not just to print something but to return a valuee


def main():
    v = get_int()
    print(f"v is {v}")
def get_int():
    while True:
        try:
            v = int(input("Give v: "))
        except ValueError:
            print("v is not an integer")
        else:
            break

    return x


main()



# we dont really need else : break right now 
# and we also dont need to define a variable if we just use it once 


def main():
    t = get_init("whats x?")
    print(f"t is {t}")
def get_init(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()



