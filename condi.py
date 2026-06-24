name = input("whats your name?: ")
#if name == "Harry":
 #print("Gryffindor")
#elif name == "Hermione":
 #print("Gryffindor")
#elif name == "Ron":
 #print("Gryffindor")
#elif name == "draco":
 #print("Slytherin")
#else:
 #print("who?")
match name:
    case "Harry":
        print("gryffindor")
    case "hermione":
        print("gryffindor")
    case "Ron":
        print("gryffindor")
    case " draco":
        print("Slytherin")
    case _:
        print("who?")

        