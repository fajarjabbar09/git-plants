import random
import json
import os


accounts ={}

def account_number():
     num = str(random.randint(1000000,9999999))
     acc_no = f"PK{num}2026"
     #prefix = "PK"
     #year = "2026"
     #acc_no = prefix + num + year
     return acc_no


def register_account(acc_no, name, password, balance = 0):
    print(" --- Account Registeration ---")
    name = input("Enter your full name: ").strip()
    password = input("Enter password: ")
    balance = int(input("Initial Deposit: "))
    acc_no = account_number()
    os.makedirs("accounts", exist_ok = True)
    filepath = f"accounts/{acc_no}.json"

    accounts[acc_no]= {
    "acc_no" : acc_no,
    "name" : name,
    "password" : password, 
    "balance" : balance
   }
    try: 
     data = json.dumps(accounts)
     with open(filepath, "x") as f:
        f.write(data)
        print(f"Account created Succeessfully!")
        print(f"Your account number is: {acc_no}")
        return True
     
    except FileExistsError:
     
        print(f"registeration failed. file already exists")
        return False

def login():
   print("--- Account Login ---")
   acc_no = input("Account number: ").strip()
   password = input("Password: ")

   if accounts["acc_no"] == acc_no and accounts[acc_no]["password"] == password:
      print(f"Login successfull.Welcome {accounts[acc_no]["name"]}!")

   else:
      print("Incorrect account number or Password")
      return None



def deposit():
   acc_no = input("Account Number: ")

   if acc_no not in accounts:
      print("Account not Found")
      return
   
   amount = int(input("Amount to deposit: "))
   if amount <= 0:
      print("Deposit must be greater than zero")
      return

   accounts[acc_no]["balance"] += amount

   print( "Deposit successful.")
   print(f"New balance: {accounts[acc_no]['balance']}")
   

def withdraw():
   acc_no = input("Account Number: ")
   if acc_no not in accounts:
      print("Account not Found")
      return
   
   amount =int(input("Amount to withdraw: "))
   if amount <= accounts[acc_no]["balance"]:
      print(f"Amount withdrawn {amount}") 
      accounts[acc_no]["balance"] -= amount
   else: 
       print("Amount Insuffient")


def main():
    print(" ---------------------- ")
    print(" Welcome to Meezan Bank ")
    print(" ---------------------- ")

    i = True
    while i:
      print("\n---- Main menu -----")
      print("1. Register")
      print("2. Login")
      print("3. Deposit")
      print("4. Withdraw")
      print("5. Exit")
      
      option = input("choose an option ")

      if option == "1":
         register_account()
      elif option == "2":
         login()
      elif option == "3":
         deposit()
      elif option == "4":
         withdraw()
      elif option == "5":
         i = False
      else:
         print("Invalid option")

main()