#python File I/0
#File Operation

#opening File
#file = open("file.txt", "r")

#Operation
#print(file.read())

#Closing File
#file.close()

# r - read mode
# w - write mode
# a - append mode
# x - create mode

try:
    file = open("creat new file", "x")
    file.write("by theary")

    #closing File
    file.close()

except FileExistsError:
    print("File already Exist")


