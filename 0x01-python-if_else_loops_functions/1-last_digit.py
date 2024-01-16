#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
print("the number is {} and the last number is {}".format(number, digit))
