from itertools import count

number: float = float(input("enter a number:"))

if number > 10:
    number = number - 10
elif number < 10:
    number = number * 10
print(f"the number is {number}")

number_list: list[float] = []
counter_num: int = 0
while True:
    number2: float = float(input("enter number"))
    counter_num += 1
    number_list.append(number2)
    if counter_num >= 3:
        break
if sum(number_list) >= 100:
    print(f"the number is {sum(number_list)}")
else:
    print("the amount is less than 100")

while True:
    age: int = int(input("enter your age:"))
    if 0 <= age <= 120:
        print(f"your age is {age}")
        break
    else:
        print("age is not in correct range")

while True:
    three_digit_number: int = int(input("enter three digit number:"))
    if 100 <= three_digit_number <= 999:
        str_convert = str(three_digit_number)
        middle_digit = str_convert[1]
        print(f" the middle digit is {middle_digit}")
        break
    else:
        print("the number is not in correct range")
