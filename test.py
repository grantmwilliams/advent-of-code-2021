from math import prod
a = list(range(1,11))
b = list(range(11, 21))

print(sum(x*y for x,y in zip(a,b)))
print(sum(a)*sum(b))