import time
import random
import sys

elements = []

i = 0
n = int(sys.argv[1])

infile = open('strings.txt')

while i < n:
	i += 1
	elements.append(infile.readline())

start = time.time()

a = elements[0]

for e in elements:
	temp = a > e

print("Python, %d elements : %f" % (n, time.time() - start))