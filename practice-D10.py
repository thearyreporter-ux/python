"""" Login System """
# build with python ddictionary 

print("********** Login *********")

profile = { "username" : "ouch sokuntheary",
            "gmail"    : "thearyreporter@gmail.com",
            "password" : "123456@"}

def login():
    attempts = 3
    while attempts >= 0:
        if attempts == 0:
           print("You can't login")
           break
        username = input("Enter Your Username: ")
        gmail = input("Enter Your gmail: ")
        password = input("Enter Your password: ")      

        if profile["username"] == username and profile["gmail"] == gmail and profile["password"] == password:
           print("You're login")
           return
        else:
           attempts -= 1
           print("try again")
                           
login()   
