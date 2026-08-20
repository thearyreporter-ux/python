# students attendance calculate systems
"""
find: total absent,total OK,total Late
"""
print("-" * 40)
print("welcome to students attendance calculator")
print("-" * 40)

# ok, late, absent
student_name = input("enter student name: ")
Total_absent= int(input("enter total absent: "))
Total_ok = int(input("enter total ok: "))
Total_late = int(input("enter total late: "))
Result = Total_absent + Total_late

print("-" * 40)

#attandance of 2026 
print(f"Total_absent: {Total_absent}")
print(f"Total_ok: {Total_ok}")
print(f"Total_late: {Total_late}")
print(f"Result: {Result}")
#rule
if Total_absent >=20:
    print("this student will be false")
elif Total_absent >=15:
    print("this student get grade re-exam")
if Total_ok >=50:
    print("this student get pass")
elif Total_ok>=60:
    print("this student get certificate")
if Total_late >=10:
    print("this student get absent for 5 times")
elif Total_late>=20:
    print("this student get absent for 10 times")
if Result >=15:
    print("this student will be re-exam")
elif Total_late>=25:
    print("this student failde the 2026 academic year")
else:
    print("INVALID")

