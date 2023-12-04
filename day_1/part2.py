#!/usr/bin/env python3

# import pdb
#
# pdb.set_trace()

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_digit(line: str):
    for i in range(len(nums)):
        if line.startswith(nums[i]):
            return (len(nums[i]), i + 1)
    return (-1, -1)


def get_digits(line: str):
    res = []
    for i in range(len(line)):
        if line[i].isdigit():
            res.append(int(line[i]))
        else:
            l, j = get_digit(line[i:])
            if l != -1:
                res.append(j)
                i += l

    return res


res = 0
with open("puzzle_input", "r") as input:
    for line in input:
        digits = get_digits(line)
        tmp = int(digits[0]) * 10 + int(digits[-1])
        print(tmp)
        res += tmp

print("Result: " + str(res))

# test = "zoneight234"
# test = replace_nums(test)
# digits = list(filter(str.isdigit, test))
# print(test, digits)
