"""
a = int(input("Число 1: "))
b = int(input("Число 2: "))
n = str(input("Операция: "))

if n == '+':
    print(a + b)
elif n == '-':
    print(a - b)
elif n == '*':
    print(a * b)
elif n == '/':
    print(a / b)

"""
"""
a = int(input("Число 1: "))
b = int(input("Число 2: "))
n = input("Операция: ")

def abc(a, b, n):
    if n == '+':
        print(a + b)
    elif n == '-':
        print(a - b)
    elif n == '*':
        print(a * b)
    elif n == '/':
        print(a / b)

abc(a, b, n)
"""

"""
a = int(input("Число 1: "))
b = int(input("Число 2: "))
n = input("Операция: ")

def abc(num1, num2, operation):
    
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)

abc(a, b, n)
"""
"""
def abc(a, b, n):
    if n == '+':
        print(a + b)
    elif n == '-':
        print(a - b)
    elif n == '*':
        print(a * b)
    elif n == '/':
        print(a / b)

while True:
    a = int(input("Число 1: "))
    b = int(input("Число 2: "))
    n = input("Операция (+, -, *, /): ")
    
    abc(a, b, n)
    
    repeat = input("Выполнить еще раз? (да/нет): ").lower()
    if repeat in ["нет", "n", "no"]:
        break
"""