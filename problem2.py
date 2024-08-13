import os
os.system("cls")
os.system("color 2")

def raqamlar(word):
    numbers = []
    number = ""

    for char in word:
        if char.isdigit():
            number += char
        else:
            if number:
                numbers.append(str(int(number)))
                number = ""

    if number:
        numbers.append(str(int(number)))

    son = set(numbers)
    
    return len(son)


word = "leet1234code234"
natija = raqamlar(word)
print(natija)
