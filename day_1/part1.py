#!/usr/bin/env python3

res = 0
with open("puzzle_input", "r") as input:
    for line in input:
        digits = list(filter(str.isdigit, line))
        res += int(digits[0]) * 10 + int(digits[-1])

print("Result: " + str(res))
