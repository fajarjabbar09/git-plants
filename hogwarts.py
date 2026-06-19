students = ["Harry", "Hermione", "Ron"]


for i in range(len(students)):
    print(i + 1 , students[i])



# hogwarts = {"Hermione": "Gryffindor", 
            # "Ron": "Gryffindor",
            # "Harry": "Gryffindor",
            # "Dracos": "Gryffindor"}
# print(hogwarts["Hermione"]) #Hermione is key and it gives its value which is gryffindor
# for hog in hogwarts:
    # print(hog, hogwarts[hog], sep =", ")
hogwarts = [
    {"name" : "Hermione", "House" :"Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "House" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "House" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    {"name" : "Draco", "House": "Slytherin", "patronus": None}
]
for hog in hogwarts:
    print(hog["name"], hog["House"],hog["patronus"], sep = ", ")


#def main():
    #print_row(4)

# def print_row(length):
    
        #print("?" * length )

#main()

def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end= "")
        print()
main()
