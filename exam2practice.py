import random
import itertools
import math
'''
Exam 2 Practice
No imports allowed unless explicitly stated
'''
'''
def randseq(n):
	import random
	seq = []
	for i in range(n):
		seq.append(random.choice('ACGT'))
	seqstr = ''.join(seq)
	return seqstr

def randnum(leng, rang):
	import random
	numlist = []
	for i in range(0, leng):
		numlist.append(random.randint(1, rang))
	return numlist

def randpro(n):
	import random
	pro = []
	for i in range(n):
		pro.append(random.choice('ACDEFGHIKLMNPQRSTVWY'))
	prostr = ''.join(pro)
	return prostr

''' # random fillers for testing
''' 
Write a function gc_comp(dna) that returns the GC composition of a nucleotide 
sequence. Use the input() function to ask the user for a sequence and then 
report its GC composition.

def gc_comp(dna):
	cg = 0
	for nt in seq:
		if nt == 'C': cg += 1
		if nt == 'G': cg += 1
	comp = cg/len(seq)
	return comp

seq = input('Input a nucleotide sequence: ')
print(gc_comp(seq), 'GC character')
''' # 21 - done
''' 
Write a function oligo_tm(dna) that computes the melting temperature of a DNA 
sequence. For oligos <= 13 nt, Tm = (A+T) x 2 + (G+C) x 4. For longer oligos, 
Tm = 64.9 + 41 x (G+C -16.4) / (A+T+G+C). Use the sys.argv as the source of 
the DNA sequence.

import sys

def oligo_tm(dna):
	at = 0
	cg = 0
	for nt in dna:
		if nt == 'A' or nt == 'T': at += 1
		if nt == 'C' or nt -- 'G': cg += 1
	if len(dna) <= 13: tm = (at)*2 + (cg)*4
	else: tm = 64.9 + 41*((cg - 16.4)/len(dna))
	return tm
	
seq = oligo_tm(sys.argv[1])
print('For a DNA sequence', len(sys.argv[1]), 'nucleotides long, the melting temperature was', seq)
''' # 22 - done
'''
Write a function crazycase() that converts a a string into aLtErNaTiNg cAsE. 
Use sys.argv to get the strings.

import sys

def crazycase(text):
	crazytext = []
	for i, letter in enumerate(text):
		if i % 2 == 0: crazytext.append(letter.lower())
		else:		   crazytext.append(letter.upper())
	crazystring = ''.join(crazytext)
	return crazystring
	
text = crazycase(sys.argv[1])
print(text)
''' # 23 - done
'''
Write a function anti(nt) that returns the reverse-complement of a DNA sequence.

def anti(nt):
	antis = []
	reverse = nt[::-1] # the sequence, backwards
	for n in reverse:
		if n.upper() == 'A': antis.append('T')
		if n.upper() == 'C': antis.append('G')
		if n.upper() == 'G': antis.append('C')
		if n.upper() == 'T': antis.append('A')
	antisense = ''.join(antis) # list into string
	return antisense

seq = 'aagtgcca'
print('The reverse-complement of the sequence', seq.upper(), 'is', anti(seq))
''' # 24 - done
'''
Write a function entropy(P) that returns the entropy of a probability distribution. 
The function should check that P sums to 1 and report an error if this is not the case.


import math
	
def entropy(P):
	total = 0
	for prob in P: total += val
	if not math.isclose(total, 1): return None
	h = 0
	for prob in P:
		h -= p * math.log2(p)
	return h

# CHECK 21entropy AND REDO IT
	''' # 25 - go over (21entropy)
'''  
Write a function maxstr(strings) that returns the string with the 
longest length in a list of strings.

def maxstr(strings):
	maxlen = len(strings[0]) # NOT 0
	maxi = 0 # cause you need the string, not just the length
	for i in range(1, len(strings)):
		if len(strings[i]) > maxlen: 
			maxlen = len(strings[i])
			maxi = i
	return strings[maxi]

applelist = ['penpinappleapplepen', 'applesauce', 'apples', 'sauce', 'this one is not about apples', 'applesauceapple',]
maxapple = maxstr(applelist)
print('the longest string is:', maxapple)
''' # 26 - done
'''
Write a function minstrlen(strings) that returns the length of the shortest 
string in a list of strings.

Write a function minstrlen(strings) that returns the length of the 
shortest string in a list of strings.

def minstrlen(strings):
	minlength = len(strings[0])
	for i in range(1, len(strings)):
		if len(strings[i]) < minlength: minlength = len(strings[i])
	return minlength
	
applelist = ['penpinappleapplepen', 'applesauce', 'apples', 'sauce', 'this one is not about apples', 'applesauceapple']
minlen = minstrlen(applelist)
print('the string with the shortest length has a length of', minlen)
''' # 27 - done
'''
Write a function minmax(X) that returns the minimum and maximum values from a 
list of numbers. You may not use max(), min(), or list methods.

def minmax(X):
	minval = X[0]
	maxval = X[0]
	for i in range(1, len(X)):
		if X[i] < minval: minval = X[i]
		if X[i] > maxval: maxval = X[i]
	return minval, maxval
	
numlist = [38, 57, 29, 64, 51, 92, 83, 16]
maxnmin = minmax(numlist)
print('the max value is', maxnmin[1], 'and the min value is', maxnmin[0])
''' # 28 - done
'''
Write a function stats(X) that returns the mean, standard deviation, 
and median for a list of numbers.

def stats(X):
	X.sort()
	n = len(X)
	midpoint = n//2
	tot1 = 0
	for x in X: tot1 += x
	mean = tot1/n
	tot2 = 0
	for x in X:
		tot2 += (x - mean)**2
	stdev = (tot2/n)**(0.5)
	if n % 2 == 1: median = X[midpoint]
	else: median = (X[midpoint] + X[midpoint+1])/2
	return mean, stdev, median
	
numlist = [38, 57, 29, 64, 51, 92, 83, 16]
stat = stats(numlist)
print('the mean is', stat[0])
print('the standard deviation is', stat[1])
print('the median is', stat[2])
''' # 29 - done
'''
Write a program colorname.py <file> <R> <G> <B> that reports the closest official 
HTML color name given some RGB values on the command line. Data is in the 
colors_extended.tsv file.
''' # 30 - ??? file reading?
'''
Write a function percent_id(s1, s2) that computes the percent identity between 
two strings of equal length (e.g. a pairwise sequence alignment).

def percent_id(s1, s2):
	if len(s1) != len(s2): return 'unequal length strings' # prob don't need on test
	same = 0
	for i in range(0, len(s1)):
		if s1[i] == s2[i]: same += 1
	percent = same/len(s1) * 100
	return percent
	
st1 = randseq(20)
st2 = randseq(20)
percid = percent_id(st1, st2)
print('the percent identity is', str(percid) + '%')
''' # 31 - done	
'''
Write a function manhattan(X1, X2) that computes the Manhattan distance 
between two lists of numbers.	
Remember it's SUM |ai - bi|

def manhattan(X1, X2):
	total = 0
	for i in range(0, len(X1)):
		dis = abs(X1[i] - X2[i])
		total += dis
	return total


X1 = randnum(20, 20)
X2 = randnum(20, 20)
manhat = manhattan(X1, X2)
print('the total manhattan distance is', manhat)
''' # 32 - done
'''
Write a function dkl(P, Q) that computes the Kullback-Leibler distance between two 
histograms. You should check that P and Q are actually histograms and you should do 
something about values of zero.

DKL(P||Q) = P(x) * math.log10(P(x) / Q(x))


def dkl(P, Q):
	# convert each histogram to probabilities
	probP = []
	probQ = []
	totP = sum(P)
	totQ = sum(Q)
	for p in P: 
		probP.append(p/totP)
	for q in Q: 
		if q == 0: sys.exit('Undefined value') # div by 0 = UD
		probQ.append(q/totQ)
	# calculate KL distance
	KL = 0
	for i in range(len(totP)):
		KL += probP[i] * math.log10(probP[i] / probQ[i])
	return KL


''' # 33 - ??? file reading - done
'''
Write a program jaccard.py <file1> <file2> that computes the Jaccard Index 
(intersection divided by union) for 2 files of names. Create your own file 
data to test your program.
''' # 34 - ??? file reading
'''
Write a function hydropathy(pro) that computes the average Kyte-Doolitle 
hydrophobicity of a protein sequence. Use the variables as defined below.

def hydropathy(pro):
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
	total = 0
	for aa in pro:
		ind = pro.index(aa) # find the location of the aa with list.index()
		total += kdh[ind] # find the corresponding value with the index
	avgkdh = total/len(pro) # find the average
	return avgkdh
	

protein = randpro(20)
KDH = hydropathy(protein)
print('the average Kyte-Doolitle hydrophobicity is', KDH)

''' # 35 - done
'''
Write a function translate(dna) that translates a nucleotide sequence into a protein 
sequence. If the codon is partial or has ambiguity symbols, translate to X. Use the 
variables defined below. The variable codons is a list of all possible codons AAA, 
AAC, AAG, AAT, ACA, ... TTT in alphabetical order.	

import itertools

def translate(dna):
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
	protein = []
	for i in range(0, len(dna), 3):
		codon = codons.index(dna[i:i+3]) # find the index using list.index(codon)
		aa = trans[codon] # use the index to find corresponding aa
		protein.append(aa) # append aa to protein
	prostr = ''.join(protein) # ''.join() to create string
	return prostr
	
	
dna = randseq(10)
pro = translate(dna)
print('the translated protein is:', pro)
''' # 36 - done	
'''
Write a program monty-pi-thon.py that estimates Pi by throwing random darts at Cartesian 
quadrant 1. Let it run infinitely. 
For inspiration see https://en.wikipedia.org/wiki/Monte_Carlo_method
distance = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
from the origin (0, 0) the cartesian distance formula is 
d = (x**2 + y**2)**(0.5)
pi/4 = inside/total
pi = 4*inside / total


import random # i assume this is allowed

inside = 0
total = 0

while True:
	x = random.random()
	y = random.random()
	dist = (x**2 + y**2)**(0.5) # cartesian distance when one point is (0, 0)
	if dist < 1: inside += 1 # if the point is within the unit circle
	total += 1
	# if total >= 1000000000: break # for testing
	pi = (4*inside)/ total
		
print('after', total, 'iterations, pi =', pi)
''' # 37 - done
'''
Write a function random_dna(n, X=[0.25, 0.25, 0.25, 0.25]) that returns a random DNA 
sequence of length n. The optional named parameter X allows the caller to specify 
weights for A, C, G, and T sequentially.	

import random # i assume this is okay
	
def random_dna(n, X=[0.25, 0.25, 0.25, 0.25]):	
	total = sum(X)
	# get proportions so we can use any weights
	pa = X[0]/total
	pc = (X[0] + X[1])/total
	pg = (X[0] + X[1] + X[2])/total # don't need pt bc it is whats left
	dna = []
	for i in range (n):
		prob = random.random()
		if   prob <= pa: dna.append('A')
		elif prob <= pc: dna.append('C')
		elif prob <= pg: dna.append('G')
		else: 			 dna.append('T')
	dnaseq = ''.join(dna)
	return dnaseq
	
Xtest = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
length = 20
dna = random_dna(length, Xtest)
print('a dna strand', length, 'nucleotides long is:', dna)
''' # 38 - done
'''
Write a function random_subseq(seq, n, k) that randomly samples a sequence, 
returning a list of n sub-sequences of length k.

def random_subseq(seq, n, k):
	subseqs = []
	for i in range(n):
		ind = random.randint(0, len(seq)-k) # end k before actual end so there are no short subseqs
		subseq = seq[ind:ind+k]
		subseqs.append(subseq)
	return subseqs
	
	
dna = randseq(20)
subs = random_subseq(dna, 5, 4)
print('from dna sequence:', dna)
print(subs)	
''' # 39 - done
'''
Write a function mutate(dna, p) that randomly mutates a DNA sequence given 
some probability p of mutation.

	
def mutate(dna, p):
	seq = list(dna) # use list(string) to make a list of letters
	for i in range(len(seq)):
		if random.random() <= p:
			seq[i] = random.choice('ACGT')
	mutdna = ''.join(seq)
	return mutdna
	
	
dna = randseq(10)
mutdna = mutate(dna, 0.5)
print(dna)
print(mutdna)	
''' # 40 - done
	
	
	
	
	
	
	
	
	
	


