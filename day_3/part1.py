#!/usr/bin/env python3


engine = open("puzzle_input", "r").read().splitlines()
res = 0


# Goal: as soon as we see a symbol other than [0-9] and '.', we search for digits around it
# if there is, we try to get the coordinates of the first digit of the associated number
# and we then put it in a set. The set will prevent us from putting the same number multiple times

coords = set()

# enumerate will output two values: i the coord and row the value
for i, row in enumerate(engine):
    for j, col in enumerate(engine[i]):
        ch = engine[i][j]

        if not ch.isdigit() and ch != '.':
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

# now, coords have all the coordinates of numbers next to a symbol
# we just have to iterate through all the coordinates,
# get the associated number and add it to a final list
# we then just have to use the sum() function

nums = []
for i, j in coords:
    num = ""
    while j < len(engine[i]) and engine[i][j].isdigit():
        num += engine[i][j]
        j += 1
    nums.append(int(num))
res = sum(nums)

# Finally, we can print the result
print("Result:", res)
