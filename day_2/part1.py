#!/usr/bin/env python3

limits = {"red": 12, "green": 13, "blue": 14}


def get_game_id(line: str) -> int:
    tokens = line.split()
    return int(tokens[1][:-1])


def verify_draw(line: str) -> int:
    draws = line.split(":")[1].split(";")

    for draw in draws:
        amounts = draw.split(",")
        for amount in amounts:
            num, color = int(amount.split()[0]), amount.split()[1]
            if limits[color] < num:
                return 0

    return get_game_id(line)


with open("puzzle_input", "r") as input:
    res = 0
    for line in input:
        res += verify_draw(line)
    print(res)
