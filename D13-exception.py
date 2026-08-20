#exception : catch error when code run so result wil not error

#number = [2,4,6]
#try:
    #print(number[3])
#except ZeroDivisionError:
    #print("cannot divide by zero")
#except IndexError:
    #print("index out of range")
#finally:
    #print("Anyway it run")

book = {
    "name": "atomic habit",
    "author": "james clear",
}
try:
    print(book["year"])
except ZeroDivisionError:
    print("cannot divide by zero")
except IndexError:
    print("index out of range")
except KeyError:
    print("key in dictionary is not found")
finally: 
    print("End of Exception")
print("Hello from exception from python")


