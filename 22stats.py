# Write a program that reports descriptive stats for numbers on the command line. 
# Your program should report the following values:
# 	The number of values
# 	The minimum and maximum values
# 	The mean and standard deviation
#	The median value

import sys

vals = []
for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(f)
# minmax
vals.sort()
minval = vals[0]
maxval = vals[-1]
# Find the average/mean
tot1 = 0
for v in vals:
	tot1 += v
mean = tot1/len(vals)
# Find the standard deviation
tot2 = 0
for v in vals:
	tot2 += (v - mean)**2
stdev = (tot2/len(vals))**(0.5)
# Find the median
midpoint = len(vals)//2
if len(vals) % 2 == 0: median = (vals[midpoint] + vals[midpoint+1])/2
if len(vals) % 2 != 0: median = vals[midpoint]

print('There are', len(vals), 'values.')
print('The minimum and maximum values are', minval, 'and', maxval)
print('The mean and standard deviation are', mean, 'and', stdev)
print('The median value is', median)




	