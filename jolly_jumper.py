# File: jolly_jumper.py
# Description: Checking if the input sequence is so called "jolly jumper"
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Checking if the input sequence is so called "jolly jumper" // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/jolly_jumper_sequence (date of access: XX.XX.XXXX)




# Implementing the task
# Checking if the input numbers are jolly jumper
# Jolly jumper is a sequence that takes all possible values from 1 to n-1
# From input neighbour elements by subtracting them
# For example input sequence 1 -3 -4 1 -1
# is jolly jumper, because result is the sequence 4 1 3 2

# Creating a list with integer numbers by inputting them in one line with gap
lst = [int(i) for i in input().split()]

# Going through the elements of the list
# Creating new list of elements that are subtraction of neighbour elements
lst_new = []
for i in range(len(lst) - 1):
    lst_new += [abs(lst[i] - lst[i+1])]

# Going through the elements of the new list
# Checking if they are from the sequence from 1 to n-1
n = 1
c = True
for x in lst_new:
    if n in lst_new:
        n += 1
    else:
        print('Not jolly')
        c = False
        break

if c:
    print('Jolly')

    
