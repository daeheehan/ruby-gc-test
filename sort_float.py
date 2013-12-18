import time
import random
import sys

elements = []

i = 0
n = int(sys.argv[1])

while i < n:
	i += 1
	elements.append(random.random())

start = time.time()
elements.sort()
print("Python, %d elements : %f" % (n, time.time() - start))