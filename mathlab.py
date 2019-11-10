import math
x =input()
y =input()

f =math.pow(int(x),int(y))
h =math.sqrt(f)
print (f)
print (h)
while h < 100000:
	h = h + 1
	print(h)
