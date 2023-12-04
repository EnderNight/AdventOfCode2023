#!/usr/bin/env python3

def get_points(line: str):
    res = 0
    line = line.split(":")[1].split('|')

    win = line[0].split()
    nums = line[1].split()

    for num in nums:
        if num in win:
            if res == 0:
                res = 1
            else:
                res *= 2

    return res


with open("puzzle_input", "r") as input:
    res = 0
    for line in input:
        res += get_points(line)

    print("Result:", res)
