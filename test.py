import random
from random import *

randomNum = randint(1, 10000)

solution = 0
a = 0
b = 0

while solution != randomNum:
	a = randint(1, 500)
	b = randint(1, 500)
	print(f"a: {a}")
	print(f"b: {b}")

	solution = a*b
	print(f"randomNum: {randomNum}")
	print(f"solution: {solution}")

print(f"\n")
print(f"solution: {solution}")
print(f"randomNum: {randomNum}")
