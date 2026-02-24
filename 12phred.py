'''
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. 
The chr() function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should return None.
'''
'''
Q + 32 = ASCII
ASCII - 32 = Q

'A' quality score = 33 quality score
restrict quality scores to 33-126
'''


def phred_to_ascii(q):
	if q < 33 or q > 126: return None
	a = q + 32
	return chr(a)

def ascii_to_phred(a):
	an = ord(a)
	if an < 33 or an > 126: return None
	q = ord(a) - 32
	return q
	
test1 = phred_to_ascii(33)
test2 = ascii_to_phred('A')
edgecase1 = phred_to_ascii(14)
edgecase2 = ascii_to_phred('~')

print('the character of phred #33 =', test1)
print("the phred value of the character 'A' is:", test2)
print('the character of phred #14 gives:', edgecase1)
print("the phred value of the character '~' is:", edgecase2)
	
