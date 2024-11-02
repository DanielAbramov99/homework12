number: int = int(input("enter your number:"))
for number in range(number, 0, -1):
    print(number, end=" ")
print()

num1: int = int(input("enter first number:"))
num2: int = int(input("enter second number:"))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)

number2: int = int(input("enter your number:"))
for x in range(1, number2 + 1):
    if x % 3 == 0 or x % 5 == 0:
        print(x)

number3: int = int(input("enter your number:"))
for z in range(1, number3 + 1):
    if z % 7 == 0:
        print(z)
