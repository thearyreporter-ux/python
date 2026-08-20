#input number
print("--------- welcome to input number ---------")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

result1 = num1 + num2
result2 = num2 + num3
result3 = num1 + num3
total = num1 + num2 + num3

print(type(result1))
print(result2)
print(result3)
print(f"total number is: {total}")