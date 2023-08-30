#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for h in range(1, 3):
        try:
            if h > a:
                raise Exception('Too far')
            else:
                result += a ** b / h
        except:
            result = b + a
            break
    return (result)
