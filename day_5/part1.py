#!/usr/bin/env python3

def get_seeds(line: str):
    res = line.split(":")[1].split()

    for i in range(len(res)):
        res[i] = int(res[i])

    return res


def get_map(line: str):
    line = line.splitlines()[1:]
    res = []

    for r in line:
        r = r.split()
        for i in range(len(r)):
            r[i] = int(r[i])

        res.append(r)

    return res


def apply_map(seed: int, maps: list[list[int]]):
    for map in maps:
        if seed >= map[1] and seed <= map[1] + map[2] - 1:
            return map[0] + (seed - map[1])

    return seed


with open("puzzle_input", "r") as input:
    seeds = []
    soil = []
    fertilizer = []
    water = []
    light = []
    temperature = []
    humidity = []
    location = []

    maps = [soil, fertilizer, water,
            light, temperature, humidity, location]
    input = input.read().split('\n\n')

    seeds = get_seeds(input[0])
    for i in range(1, len(maps)):
        maps[i - 1] = get_map(input[i])

    for i in range(len(seeds)):
        for j in range(len(maps)):
            seeds[i] = apply_map(seeds[i], maps[j])

    print("Result:", min(seeds))
