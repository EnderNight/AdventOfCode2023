#!/usr/bin/env python3

engine = open("puzzle_input", "r").read().splitlines()
res = 0

# The algorithm is quite the same as in part1


# enumerate will output two values: i the coord and row the value
for i, row in enumerate(engine):
    for j, col in enumerate(engine[i]):
        ch = engine[i][j]

        # instead of getting every number arround symbols, we only want numbers around '*'
        if ch == '*':
            # now that we have to verify the number of numbers around a '*'
            # having a global set will be difficult. Thus, we'll use a set per '*'
            coords = set()
            for ii in [i - 1, i, i + 1]:
                for jj in [j - 1, j, j + 1]:
                    # we have to verify if we are in bounds
                    # since we are in a loop, we have to verify for every bound
                    if ii >= 0 and ii <= len(engine) - 1 and jj >= 0 and jj <= len(engine[ii]) - 1:
                        # Then, if the current character is a digit, we have to add its coordinates to the set
                        if engine[ii][jj].isdigit():
                            # We need to get the cooordinates of the first digit, thus we have to verify if we are
                            # at the beginning of the line
                            while jj > 0 and engine[ii][jj - 1].isdigit():
                                jj -= 1

                            # now that we have found the first digit, we add the coordinates to the set
                            coords.add((ii, jj))
            # After getting all numbers, we can verify of there is actually two
            # if there is, we can add them to the final result
            nums = []
            if len(coords) == 2:
                for ii, jj in coords:
                    num = ""
                    while jj < len(engine[ii]) and engine[ii][jj].isdigit():
                        num += engine[ii][jj]
                        jj += 1
                    nums.append(int(num))
                res += nums[0] * nums[1]

# Finally, we can print the result
print("Result:", res)
