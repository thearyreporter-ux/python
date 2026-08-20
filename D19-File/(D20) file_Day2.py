#using with statment

#ith open("new_text.txt", "x") as file:
   #file.write("new text file Created")

FILE_NAME = "new_text.txt"
CREATE_MODE = "a"
READ_MODE = "r"

with open(FILE_NAME,CREATE_MODE) as file:
    file.write("new text file created\n")

with open(FILE_NAME, READ_MODE) as file:
    files = file.readlines()
    for i in files:
       print