#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
prefix = "and is less than 6 and not 0"
if last > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, last))
if last == 0:
    print('Last digit of {} is {} and is 0'.format(number, last))
if last < 6:
    print('Last digit of {} is {} {}'.format(number, last, prefix))
