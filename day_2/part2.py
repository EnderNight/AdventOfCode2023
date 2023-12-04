#!/usr/bin/env python3

def get_power(amounts: dict):
    res = 1
    for color in amounts:
        res *= amounts[color]
    return res


def get_max(line: str):
    res = {"red": 0, "green": 0, "blue": 0}
    draws = line.split(":")[1].split(";")

    for draw in draws:
        amounts = draw.split(",")
        for amount in amounts:
            num, color = int(amount.split()[0]), amount.split()[1]
            if res[color] < num:
                res[color] = num

    return get_power(res)


with open("puzzle_input", "r") as input:
    res = 0
    for line in input:
        res += get_max(line)
    print(res)
