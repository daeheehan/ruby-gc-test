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
elements.sort()
print("Python, %d elements : %f" % (n, time.time() - start))