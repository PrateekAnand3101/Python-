from queue import PriorityQueue

firstno = input("Enter first number: ")
op = input("enter operator(+,-,/,*,%): ")
secondno = input("enter second number: ")
firstno = int(firstno)
secondno = int(secondno)
if op == '+':
    print(firstno + secondno)
elif op == '-':
    print(firstno - secondno)
elif op == '*':
    print(firstno * secondno)
elif op == '/':
    print(firstno / secondno)
elif op == '%':
    print(firstno % secondno)
else:
    print("Invalid Input")

#range function
number = range(5)
print(number)