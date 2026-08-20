""" This is teachers management system """

list_teachers = ["Hong", "Nika", "Meng", "reach"]

while True:
    def display():
        print("=="*20)
        print("    welcome To teachers Management")
        print("=="*20)
        print("1. view teachers")
        print("2. add teachers")
        print("3. update teachers")
        print("4. delete teachers")
        print("5. successfully!")

        option= int(input("Pleas Enter Your Option (1-4): "))
        match option:
            case 1:
                view_teachers()
            case 2:
                add_teachers()
            case 3:
                update_teachers()
            case 4:
                delete_teachers()
            case 5:
                successfully()

    def view_teachers():
        if len(list_teachers) == 0 :
           print("teacher not found")
        print(list_teachers)

    def add_teachers():
        name = input("Enter teacher name: ")
        list_teachers.append(name)
        print("teacher added successfully")

    def update_teachers():   
        name = input("Find teacher name: ")
        if name in list_teachers:
            print("Teacher exist")
            new_name = input("teacher new name: ")
            print("teacher updated successfully")
        else :
            print("teacher name Not Found")

    def delete_teachers():
        name = input("Enter teacher name u want to delete: ")
        print("teacher name delete successfully")

    def successfully():
        print("You're success")

    display()