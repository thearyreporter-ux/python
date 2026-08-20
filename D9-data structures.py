#set: RANDOM
student = {10001, "kaka", "artist", 21, 21, "kaka"}
print(student) #unduplicated no the same ans

#avoid duplicate
classroom = {101, "data structure", "ka"}
classroom.add("python")
classroom.add("data science")
classroom.add("50")
classroom.add("50")
classroom.remove(101)
classroom.discard("10") #if we put it when value don't have in set ans will not error as remove
print(len(classroom)) #find ប្រវែង set
print(classroom)

#set union
a = {1,2,3}
b={4,5,6,7}
c =a.union(b)
d = {9,0,10}
#print(c)
C = a|b|d

#intersection : ប្រសព្វ
a={1,2,3,4,5}
b={2,3,4,5}
#e = a.intersection(b)
e = a&b

#difference
i = {1,2,3,4,5}
j={1,2,3,4,5,6,6,8,9}
#k = i.difference(j)
k = j - i
print(k)