# Data structure
# List: store multiple item in one variable and index start with 1

#square Bracket
numbers = [1, 2, 3, 4 ,5]  #index start with zero
print(numbers)

numbers = [1, 2, 3, 4 ,5] #ans lek 4 cuz index start from 0
#print(numbers[5])

numbers = [1, 2, 3, 4 ,5] # index start from the last one
print(numbers[-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 12, 13, 14]
print(f"{numbers[len(numbers)-1]}") #if not put -1 it's will error
# or print(numbers[len(numbers)-1])

# membership
print(12 in numbers) #ans True if have
print (numbers[1])

bucket = []
bucket.append("milk")  #add in list
bucket.append("meat")
bucket.append("egg")

bucket.remove("milk")  #delete in list
bucket.insert(1, "water")  #add in any place in list that we want like num 1 is place we add
bucket.pop()   # delete last one if we put number in (1, ...), also delete
print(bucket)


#tuple: immutable that store multiple items (can't change data)
person = ("kaka", 20, "siem reap", True)
#persion[1] = 18 ,  ans error cuz we can't edit the immutable but list we can
print(person)

#set
student = [10,12,45,10,24]
print(student)