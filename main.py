print("Hello there, you need to connect to your account to use this website! \n")

password_length = 8

def debut():
    choose = input("Do you want to login or to create an account (login, new account) : ").lower()
    if choose == "login":
        login()
    elif choose == "new account":
        new_account()

def new_account():
    email = input("Email : ")
    confirm_email = input("Pls confirm Email: ")
    if confirm_email == email:
        age = int(input("How old are you: "))
        if age >= 18:
            password = input("Create a new password of 8 characters minimum : ")
            confirm_password = input("Confirm the password : ")
            if confirm_password == password and len(confirm_password) >= password_length:
                file_write = open('login.txt', 'w')
                choose_username = input("Choose a username : ")
                file_write.write(f'{choose_username} \n')
                file_write.write(confirm_password)
                file_write.close()
            else:
                print("The passwords doesn't match, or it's too short")
                new_account()
        else:
            print("You can't create an account if you're under 18")
            new_account()
    else:
        print("The emails doesn't match")
        new_account()


def login():
    username = str(input("Username : "))
    password = str(input("Password : "))
    file = open('login.txt', 'r')
    lines = file.readlines()

    newList = []
    for each_line in lines:
        newList.append(each_line.strip())

    file = open('login.txt', 'r')
    lines = file.readlines()

    newList = []
    for each_line in lines:
        newList.append(each_line.strip())
    if username == newList[0] and password == newList[1]:
        print("You are connected successfully")
    else :
        print("The username or the password is incorrect, pls try again")
        login()


debut()
