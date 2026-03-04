import math
import argparse
''' Demo, practice, and in-class notes for Unit 3'''
'''
# Exam will probably only go from 41 to 49
# Practice Exam 3 Question 45

# Write a function polya(dna) that returns the length of the longest 
# stretch of As in a dna sequence.

# seq = 'ACGTAAAACACCAGAGTCAAAAAAACGATA'


for i in range(len(seq)):
	nt = seq[i] == 'A': print(i)
	
for i, nt in enumerate(seq):
	if nt == "A": print(i)
	
while True	
	for i in range(len(seq)):
		a_count = 0
		if seq[i] == 'A':
			if seq[i+1] == 'A'
		
seq = 'ACGAAACTAT' = 0
max_run
max_pos = 1
i = 0

while i < len(seq):
	if seq[i] == 'A':
		run_start = i
		run_len = 1
		for j in range(i+1, len(seq)):
			if seq[j] == 'A': run_len += 1
			else: break
		i = j
		print(run_start, run_len)
		#if run_len > max_run: 
		#	max_run = run_len
		#	max_pos = run_start
	i  += 1
''' # Notes 3/3
'''
write a program Fizzprime.py
 - prints the numbers 1-100
 - if the number is prime, print 'fizz' after it
 - run the program
 - pipe it to grep and remove all non-fizz lines
 - redirect the output to a file: fizz.txt

def is_prime(x):
	for n in range (2, x//2):
		if x % n == 0: return False
	return True

for i in range(100):
	if is_prime(i) == True: print(i, 'fizz')
	
#py | grep -v fizz > fizz.txt
''' #fizzprime with grep
'''
def entropy(s):
	tot = len(s)
	pa = s.count('A')/tot
	pc = s.count('C')/tot
	pg = s.count('G')/tot
	pt = s.count('T')/tot
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h
seq = 'ACGTAAAAAAACGTACGT'
sed = list(seq)
k = 7

parser = argparse.ArgumentParser()
#parser.add_argument('fasta')
parser.add_argument('k', type=int, default=7)
parser.add_argument('seq')
parser.add_argument('--threshold', type=float, default=1.0, help='%(default).3f')
parser.add_argument('--soft', action='store_true')
arg = parser.parse_args()
	
# for defline, seq in

for i in range(len(seq) -k+1):
	subseq = seq[i:i+k]
	if entropy(subseq) < arg.threshold:
		for j in range(i, i+k):
			if soft: sed[j] = sed[j].lower()
			else: sed[j] = 'N'
PRINT(''.join(sed))
	




def dust(deq, k, t):
	sed = list(seq)
	for i in range(len(seq) -k+1):
		if entropy(seq[i:i+k] < t):
			for k in range(i, i+k):
				sed[j] = 'N'
''' # dust, entropy filter (E3Q49)
''' # wow
	# inefficient
def myentropy(s):
	ntlist = []
	ntcount = []
	ntprob = []
	for i in range(0, len(s)):
		nt = s[i]
		if not nt in ntlist: ntlist.append(nt)
		else: ntcount[ntlist.index(nt)] += 1
	for num in ntcount:
		prob = num/sum(ntcount)
		ntprob.append(prob)
	# ughhhhh
''' #really inefficient entropy calc (mine)
'''
# the function, exactly as I wrote it out on the exam
def crazycase(string):
	words = list(string)
	for i, letter in enumerate(words):
		if i % 2 == 0: words[i] = letter.lower()
		else: 		   words[i] = letter.upper()
	crazystring = ''.join(words)
	return crazystring
	
string1 = 'this is a test'
string2 = 'oooooooooo spooky'
string3 = 'then why did i get this wrong'
print(crazycase(string1))
print(crazycase(string2))
print(crazycase(string3))
''' # test question WRONG??
