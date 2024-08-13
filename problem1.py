import os
os.system("cls")
os.system("color 2")

def sonlar(lst):
    son = {}
    for num in lst:
        if num in son:
            son[num] += 1
        else:
            son[num] = 1
    
    counts = []
    for count in son.values():
        if count in counts:
            return False
        counts.append(count)
    
    return True

print(sonlar([1, 2, 2, 3, 3, 3])) #True
print(sonlar([1,2]))  # False
