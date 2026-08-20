print("********** Welcome **********")

num = [1,3,5,7,9]
print(num[2])
skincare = {
    "sunscreen": "medicube",
    "serum": "torriden",
    "toner": "numbuzin",}
try:
    print(skincare["serum"])
except ZeroDivisionError:
    print("cannot divide by zero")
except IndexError:
    print("index out of range")
except KeyError:
    print("key in dictionary is not found")
finally: 
    print("End of Exception")
print("Hello from exception from python")

print("-------------------------------")

print(input("Enter your age: "))
age = 17
if age <= 18:
    false ValueError("You are not eligible to work")
else:
    print("You're eligible to work")