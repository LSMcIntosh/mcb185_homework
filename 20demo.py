import math
import sys
import random
import itertools

'''
print(f'{math.sqrt(25)}')
print(f'{"hello world":.<20}')
print(f'{"hello again":.^20}')
print(f'{"hello again":.>20}')
print(f'{20:<10} {10}')
''' # print(f'{}') practice
'''
people = int(sys.argv[1])		
calendar = int(sys.argv[2])		
iterations	= int(sys.argv[3])

for _ in range(iterations):
	classroom = []		
	same_birthday = False
	for i in range (people):
		birthday = random.randint(0, calender-1)
		if birthday in classroom:
			same_birthday = True
			break
		classroom.append(birthday)	
	if same_birthday: sames += 1
		
		
		
classroom = ['A', 'B', 'C', 'D']		
for i range(0, len(classroom)):		
	for j in range(i+1, len(classroom)):	
		print(classroom[i], classroom[j])
		
same_birthday = False		
for i range(0, len(classroom)):		
	for j in range(i+1, len(classroom)):	
		if classroom[i] == classroom[j]: same_birthday = True
	if same birthday: sames += 1

probability = sames/iterations  # probability of a same birthday

# probability of same birthday

calendar = [0] 
''' # 2/12/26 Notes
'''
def translate(orf):
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
	protein = ''
	for i in range(0, len(orf), 3):
		codon = orf[i:i+3]
		idx = codons.index(codon)
		aa = trans[idx]
		protein += aa
	return protein


protein = translate('ATAGCGAAT')
print(protein)

#def rand_sequence(n):
#for i in range (0, 3*n):
#	nb = random.randint(1, 4)
#	if nb == 1: sequence += 'A'
#	if nb == 2: sequence += 'C'
#	if nb == 3: sequence += 'G'
#	if nb == 4: sequence += 'T'
# my try for a random nb sequence

def anti(seq):
	rev = seq[::-1]
	rc = ''
	for nt in rev:
		if   nt == 'A': rc += 'T'
		elif nt == 'C': rc += 'G'
		elif nt == 'G': rc += 'C'
		elif nt == 'T': rc += 'A'
	return rc



seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def random_subseq(seq, n, k):
	subs = []
	for i in range(n):
		x = random.randint(0, len(seq) -k)
		subseq = seq[x:x+k]
		if random.random < 0.5: subseq = anti(subseq)
		subs.append(subseq)
	return subs
''' # 2/19/26 Notes p1
'''
test test

def mutate(s, p):
	seq = list(s)
	for i in range(len(seq)):
		if random.random < p:
			seq[i] = random.choice('ACGT')

dna = 'AAAAAAAAAAAAAAAAA'
dna = mutate(dna, 0.2)
print(dna)
	

def random_dna(n, X = [0.25, 0.25, 0.25, 0.25]):
	#if not math.isclose(1.0, sum(X)): sus.exit('oops')
	total = sum(X)
	a = X[0]/total
	c = (X[0] + X[1])/total
	g = (X[0] + X[1] + X[2])/total
	rseq = ''
	for i in range(n):
		r = random.random()
		if   r < a: rseq += 'A'
		elif r < c: rseq += 'C'
		elif r < g: rseq += 'G'
		else: 		rseq += 'T'

for i in range(5):
	print(i, random_dna(10))
''' # 2/19 Notes p2
'''

''' # wow more notes p3
'''
alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

# print header
print('    ', end='')
for c in alph: print(c, end=' ')
print()
	
# print body
for i in range(len(alph)):
	# print the leading letter
	print(alph[i], end='')
	# print the row
	for j in range(len(alph)):
		if i == j: print(mat, end=' ')
		else: print(mis, end=' ')	
	print() # end the row
''' # matrix 
'''

# Write a function that returns the minimum value of a list.
def list_minimim(vals):
	vals.sort()
	return vals[0]

# Write a function that returns the minimum and maximum value of a list.
def list_minmax(vals):
	vals.sort()
	return vals[0], vals[-1]

# Write a function that returns the mean of the values in a list.
def list_mean(vals):
	total = 0
	n = 0
	for value in vals:
		total += value
		n += 1
	mean = total/n
	return mean
	
# Write a function that computes the entropy of a probability distribution.


# Write a function that computes the Kullback-Leibler distance between 
# two sets of probability distributions.
''' # practice problems unit 2




