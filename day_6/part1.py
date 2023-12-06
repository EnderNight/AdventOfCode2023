#!/usr/bin/env python3

def get_num_wins(time: int, dist: int):
    shortest = 0
    longest = 0

    tmp_time = 0
    while shortest < dist and tmp_time < time - 1:
        tmp_time += 1
        speed = tmp_time
        remaining = time - tmp_time
        shortest = remaining * speed
    shortest = tmp_time
    longest = time - shortest

    return longest - shortest + 1


with open("puzzle_input", "r") as input:
    input = input.read().strip().splitlines()

    times = input[0].split(":")[1].split()
    dists = input[1].split(":")[1].split()

    res = 1

    for i in range(len(times)):
        res *= get_num_wins(int(times[i]), int(dists[i]))

    print("Result:", res)
