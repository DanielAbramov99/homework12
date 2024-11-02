negative_list: list[int] = []
while True:
    number: int = int(input("enter a number:"))
    if number == 0:
        break
    else:
        if number < 0:
            negative_list.append(number)
print(f" the summary number of all negative numbers combined is {sum(negative_list)}")

numbers_list: list[int] = []
for num in range(10):
    number1: int = int(input("enter a number:"))
    numbers_list.append(number1)
print(numbers_list)
print(numbers_list[::-1])

prime_number_list: list[int] = []
while True:
    number2: int = int(input("enter a number:"))
    if number2 == 0:
        break
    else:
        if number2 == 1:
            continue
        elif number2 == 2:
            prime_number_list.append(number2)
        elif number2 % 2 == 0:
            continue
        else:
            divider: int = 3
            found: bool = False
            while divider < number2 ** 0.5 + 1:
                if number2 % divider == 0:
                    found = True
                    break
                divider += 2
            if not found:
                prime_number_list.append(number2)
print(prime_number_list)
print(f"the amount of prime numbers is {len(prime_number_list)}")

import statistics

avg_list: list[float] = []
above_avg: int = 0
for n in range(5):
    number3: float = float(input("enter a number:"))
    avg_list.append(number3)
avg_num: float = statistics.mean(avg_list)

for a in range(len(avg_list)):
    if avg_list[a] > avg_num:
        above_avg += 1
print(avg_list)
print(
    f"the average of this list is {avg_num} and the amount of numbers in the list that are above average is {above_avg} ")

# אני לא כל כך הבנתי מה זאת אומרת בהפחתות בלבד אז פתרתי את זה ככה
num1: int = int(input("enter first number:"))
num2: int = int(input("enter second number:"))
div: float = num1 // num2
print(div)
