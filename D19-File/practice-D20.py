"""
User Contact Program
Objective
1. Save contact in the file
2. View All contact in the file

"""

def Create_contact():
    username = input("Enter Username: ")
    phone = input("Enter phone number: ")
    with open("contact.txt", "a") as file:
        file.write(f"{username}, {phone}\n")
    print("New Contact Created successfully!")


def view_contact():
    with open("contact.txt", "r") as file:
        if not file:
            print("No contact saved")
        for line in file:
            username, phone = line.strip().split(",")
            print(f"username: {username}, phone: {phone}")

def main():
    while True:
        print("1. view Contacts")
        print("2. save contact")
        print("3. exit")

        choice = input("Enter choice (1-3): ")
        match choice:
            case "1":
                view_contact()
            case "2":
                Create_contact()
            case "3":
                print("Exiting Program...")
                break
            case _:
                print("Invalid")

if __name__ == "__main__":
    main()


        