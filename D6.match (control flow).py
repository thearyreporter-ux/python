# match (control flow)
day = "wednesday" #if we put monday result is nothing
match day:
    case "wednesday":
        print("today is working day")
    case "thursday":
        print("today is working day")
    case ("saturday"):
        print("today is relax day")
    case ("sunday"):
          print("today is holiday")
    case _:
        print("INVALID")


#for loop statemnet
for i in range(1,11):
    print(i)

for i in range(0,5):
    print(f"{i + 1}. hello")

for i in range(10, 0,-2):
    print (i)

#while loop
i = 5
while i>0:
    print("yes i is bigger than zero")

#infinite loop
i = 5
while i > 0:
    print(f"{i}. Yes i is bigger than Zero")
    i -=1
    