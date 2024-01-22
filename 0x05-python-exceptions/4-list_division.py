#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newL = []
    x = 0
    while x < list_length:
        try:
            newL.append(my_list_1[x] / my_list_2[x])
        except (TypeError, ValueError):
            print("wrong type")
            newL.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newL.append(0)
        except IndexError:
            print("out of range")
            newL.append(0)
        x += 1
    return newL

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
