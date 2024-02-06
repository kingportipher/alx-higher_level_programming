#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    try:
        for i in range(1, 3):
            result += a ** i + b ** i
    except TypeError:
        print("Type error occurred!")
    return result
