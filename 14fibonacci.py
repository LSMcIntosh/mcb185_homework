# write a program that reports the first 10 numbers from the Fibonacci sequence: 
# 		0, 1, 1, 2, 3, 5, 8, 13, 21, 34

a = 0
b = 1
for i in range (10):
	print (a, end=" ")
	c = a + b
	a = b
	b = c
print ("")
