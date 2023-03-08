#!/usr/bin/python3
# This code will define the randomly generated code is weather negetive, zero or positive
import random
number = random.randint(-10, 10)
if number < 0:
    print('is negative \n')
elif number == 0:
    print('is zero \n')
else:
    print('is positive \n')
