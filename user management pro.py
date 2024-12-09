import os
import time

# انشاء كلاس يوزر
class User:
    def __init__(self, first_name, last_name, email, password, ID, status = "inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.ID = ID
        self.status = status
    
    # عرض معلومات الحساب
    def display_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"ID: {self.ID}")
        print(f"Status: {self.status}")

print("Welcome To User Management!...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    #انشاء حساب جديد
def creat_user():
    first_name = input("Enter the first name: ").lower()
    last_name = input("Enter the last name: ")
    ID = input('Enter the user ID: ')
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    status = input("Enter user status: ").lower()

    return User(first_name, last_name, ID,  email, password, status)
 # البحث عن حساب
def serch_user(users):
    clear_screen()
    print("you serch whit:\n1- user name\n2- user ID\n3- user status")
    serch_methode = input("Enter your choice: ")
    found_member = []
    print("_"*20)
    
    if serch_methode == "1":
        serch_name = input("Enter the user name: ")
    
        for x in users:
            if x.first_name == serch_name.lower():
               found_member.append(x)
    
    elif serch_methode == "2":
        serch_id = input("Enter the user ID: ")
        
        for x in users:
            if x.ID == serch_id:
                found_member.append(x)
                break

    elif serch_methode == "3":
        serch_member = input("Enter the user status: ")

        for x in users:
            if x.status == serch_member.lower():
                found_member.append(x)
    else:
        print("Invalide choice")

    if found_member:
        clear_screen()
        print("Members found: ")
        
        for x in found_member:
            x.display_user()
    else:
        print("user not found")
        time.sleep(2)
     
    return users

    


users = []
while True:
    print("_"*30)
    print("1- New user\n2- Chow users\n3- serch user\n4- exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        clear_screen()
        time.sleep(0.5)
        users.append(creat_user())
        
        print("User added sucsesfully...")
        print("_"*20)
        
    elif choice == "2":
        clear_screen()
        if users:
            
            print("Displaying users ....")
            time.sleep(1)
            for i in users:
                print("_"*20)
                i.display_user()
        else:
            print("_"*20)
            print("You don't have any user")

    elif choice == "3":
        if users:
            serch_user(users)          
        else:
            print("_"*40)
            print("I don't have any think to display")    
            print("_"*40)

    
    elif choice == "4":
        print("Exiting ....")
        time.sleep(1)
        break
    else:
        print("Invalide choice, try again")

