from operation import sum, sub, mul, div
from display import show_results

list_operation = [sum, sub, mul, div]

data = { 100 : 80,
         90 : 70,
         80 : 60,
         70 : 10}

for operation in list_operation:
    for key, value in data.items():
        print(show_results(operation(key, value)))

print(show_results(sum(10, 50)))
print(show_results(sub(30, 6)))
print(show_results(mul(13, 7)))
print(show_results(div(100, 20)))