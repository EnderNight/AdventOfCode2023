#!/usr/bin/env python3

def get_num(input: list[str], i: int, res: list[int]):

    line = input[i].split(":")[1].split("|")

    count = 0
    win = line[0].split()
    nums = line[1].split()

    for num in nums:
        if num in win:
            count += 1

    for k in range(res[i]):
        for j in range(count):
            res[i + j + 1] += 1

    return res


with open("puzzle_input", "r") as input:
    input = input.read().splitlines()
    res = [1] * len(input)
    for i in range(len(input)):
        res = get_num(input, i, res)
    print("Result:", str(sum(res)))
