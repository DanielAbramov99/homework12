while True:
    num: int = int(input("enter a number:"))
    save: int = num
    sum_digit: int = 0
    print(num, ": ", end="")
    if 100 <= num <= 999:
        pass
    else:
        print("invalid number, enter three digit number please")
        continue
    while num > 0:
        ahadot: int = num % 10
        sum_digit += ahadot
        num = num // 10
        print(f"{ahadot} {"+ " if num > 0 else "= "}", end="")
    print(sum_digit)
    if sum_digit % 3 == 0:
        print("can be divided by 3")
    else:
        print("cannot be divided by 3")
    break


def bacwards(word):
    word = word.lower()
    return word == word[::-1]


word: str = str(input("enter your word:"))
if bacwards(word):
    print(f"'{word}' can be spelled backwards.")
else:
    print(f"'{word}' cannot be spelled backwards.")
