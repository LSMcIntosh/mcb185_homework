import sys
import math

probs = []
for arg in sys.argv[1:]: # reads all arguments except filename
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
	probs.append(f)

prob = 0
for p in probs: prob += p
if not math.isclose(prob, 1): sys.exit('error: total probabilty is not 1')

h = 0
for p in probs:
	h -= p * math.log2(p)

print(f'{h:.4f}')
