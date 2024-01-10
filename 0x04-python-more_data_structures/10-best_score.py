#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bestSC = 0
    bestSK = None
    for n, i in a_dictionary.items():
        if i > bestSC:
            bestSC = i
            bestSK = n
    return bestSK
