__author__ = 'daemoniclegend'

'''
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four
million, find the sum of the even-valued terms.
'''


class Problem2:

    __first = 1
    __second = 2
    __third = 0
    __sum = 2

    while __third < 4000000:
        __third = __first + __second
        if __third % 2 == 0:
            __sum += __third

        __first = __second
        __second = __third

    print(__sum)

    def __init__(self):
        pass
