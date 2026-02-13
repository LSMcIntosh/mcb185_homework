'''
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. 
The chr() function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should return None.
'''

'''
As per the wikipedia page for 'Phred quality score':
Phred quality scores (Q) and base-calling error probabilities P are related by
Q = -10 log(P)
P = 10^(-Q/10)

ASCII valie - 32 = quality value symbol

'A' quality score = 33 quality score
33-126 or restrict to 50
'''

'''
Q + 32 = ASCII
'''


import math

def phred_to_error(Q):
	P = 10 ** (-Q / 10)
	return P
	

def error_to_phred(P):
	if P <= 0: return None
	Q = -10 * math.log10(P)
	return Q
	
test1 = phred_to_error(10)
test2 = error_to_phred(0.1)
edgecase1 = phred_to_error(0)
edgecase2 = error_to_phred(0)

print ("Test 1: A phred value of Q10 =", test1)
print ("Test 2: An error rate of 0.1 = Q" + str(int(test2)))
print ("Test 3: A phred value of Q0 =", edgecase1)
print ("Test 4: An error rate of 0 returns", edgecase2)
