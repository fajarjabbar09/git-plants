#-------------------------------------------MATCH STATEMENT---------------------------------
# Value of the xpression is compared with the values of each case
# associated block of code is executed
day = 4
match day:
     case 1:
          print("Monday")
     case 2:
          print("Tuesday")
     case 3:
          print("Wednesday")
     case 4:
          print("Thursday")
     case 5:
          print("Friday")
     case 6:
          print("Saturday")
     case 7:
          print("Sunday")



day = 5 
match day:
     case 6:
          print("Today is Saturday")
     case 7:
          print("Today is Sunday")
     case _:
          print("Looking forward to the weekend")   # should be kept as the last case beacuse it always matches




# ---- Combine values ----
day = 4
match day:
     case 1 | 2 | 3 | 4 | 5:
          print("Today is a weekday")
     case 6 | 7:
          print("I love Weekends!")



# If Statement in the caes evaluation as an extra condition check

month = 5
day = 4
match day:
     case 1 | 2 | 3 | 4 | 5 if month == 4:
          print("A weekday in April")
     case 1 | 2 | 3 | 4 | 5 if month == 5:
          print("A weekday in May")
     case _:
          print("No match")

          