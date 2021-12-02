"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""


from functools import reduce

"""
Container hints:
x = (aim, horizontal, depth)
y = (command, units)
"""
ans = reduce(
    lambda x,y: (x[0]+y[1],x[1],x[2]) if y[0] == "down" else (x[0]-y[1],x[1],x[2]) if y[0] == "up" else (x[0],x[1]+y[1],x[2]+x[0]*y[1]),
    [(l[0], int(l[1])) for l in map(str.split, open("advent-of-code-2021/inputs/day02.txt"))],
    (0, 0, 0)
)
print(f"Day2 - Part 1: {ans[1]*ans[0]}")
print(f"Day2 - Part 2: {ans[1]*ans[2]}")