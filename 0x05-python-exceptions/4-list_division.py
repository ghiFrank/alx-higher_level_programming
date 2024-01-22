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
