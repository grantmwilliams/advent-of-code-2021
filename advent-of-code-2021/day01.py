"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""

from aocd import numbers

p1 = sum(y>x for x,y in zip(numbers, numbers[1:]))
p2 = sum(y>x for x,y in zip(numbers, numbers[3:]))
print(f"Day1 - Part 1: {p1}")
print(f"Day1 - Part 2: {p2}")
