#Function python

def show_name():
    print(f"hello")

#calling function
show_name()

#function with parameter
def greeting(name, age):
    print(f"hello {name}, welcome to python")
    print(f"Your age {age}")
greeting ("kaka", 6)


# calculation

print("Welcome To Calculator")
print ("*"*40)
def show_info():
    print("---------- Calculator ----------")
    print("1. Add        (+)")
    print("2. Subtract   (-)")
    print("3. Multiply   (*)")
    print("4. Divide     (/)")
    print("5. Exit")
    

def operate():
    option = input("enter your option (1-5): ")
    match option:
        case "add":
            num1 = int(input("Enter num1 = "))
            num2 = int(input("Enter num2 = "))
            total = num1 + num2
            print(f"total number = {total}")
        case "subtract":
            num1 = int(input("Enter num1 = "))
            num2 = int(input("Enter first num2 = "))
            total = num1 - num2
            print(f"total number = {total}")  
        case "multiply":  
            num1 = int(input("Enter num1 = "))
            num2 = int(input("Enter num2 = "))
            total = num1 * num2
            print(f"total number = {total}")     
        case "divide":  
            num1 = float(input("Enter first num1 = "))
            num2 = float(input("Enter first num2 = "))
            total = num1 / num2
            print(f"total number = {total}")
        case _:
            print("invalid option")
while True:
    show_info()
    operate()