# from multiprocessing.reduction import duplicate

numbers = [1, 2, 2, 3, 4, 4]
se = set()
duplicates  = set()
for num in numbers:
    if num in se:
        duplicates.add(num)
    else:
        se.add(num)
print(duplicates)

