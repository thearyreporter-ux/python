#logical operator
a = 20
b = 30

#comparison (and)
print(a>b and b>a) #false cuz in py will false one of them wrong if true all and will true 
print(a<=b and b>a) #true

#comparison (or)
num1 = 5
num2 = 10
result1 = num1 == num2
result2 = num1 >= num2
result3 = num1 <= num2
print (result2 or result3) #true if one if them true ans will be true
print(result1 or result2) #FALSE

#comparison (not)
status = True
print(not status)

#conditional statement (if)
age = 16
if age >= 18:
      pass # if we not put pass it will be error
    print("you are eligible to vote")
print("code work normal") #it's not working in if cuz it outside if

if age > 60:
    print("you are not eligible to vote")