import math


def mean(list_input):
    total = 0
    for i in list_input:
        total += i
    return total/len(list_input)


def variance(list_input):
    data_mean = mean(list_input)
    total = 0
    for i in list_input:
        total += math.pow((i - data_mean), 2)
    return total/(len(list_input) - 1)