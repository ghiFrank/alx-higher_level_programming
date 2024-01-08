#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    newL = []
    for n in my_list:
        if n % 2 == 0:
            newL.append(True)
        else:
            newL.append(False)
    return newL

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1