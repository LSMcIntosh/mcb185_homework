''' Exam 3 Practice - No imports allowed unless explicitly stated '''
'''
Write a program print_matrix.py <alphabet> <plus> <minus> that displays a simple 
scoring matrix for matches and mismatches. The program must have the alphabet and 
scores as command line arguments. Given the command line shown, the output should 
match exactly.

import sys
alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('   ', end='')
for letter in alph: print(letter, end='  ')
print()
for i in range(len(alph)):
	print(alph[i], end=' ')
	for j in range(len(alph)):
		if alph[i] == alph[j]: print(mat, end=' ')
		else:				   print(mis, end=' ')
	print()
''' # 41 - print_matrix.py										41	DONE
'''
Write a program triples.py <n> that finds all Pythagorean Triples with sides from 
1 to n (e.g. 100). There should be no duplicates. For example, 3-4-5 is a Pythagorean 
Triple, but 4-3-5 is really the same thing and should not be reported.

import sys

n = int(sys.argv[1])
for a in range(1, n):
	for b in range(a, n):
		c = (a**2 + b**2)**(0.5)
		if c % 1 != 0: continue
		print(a, b, int(c))
''' # 42 - Pythagorean Triples									42	DONE
'''
import sys
import random

num_days = int(sys.argv[1])
num_people = int(sys.argv[2])
birth_count = 0
trials = 50
for _ in range(trials):
	birthdays = []
	same_birthday = False
	for person in range(num_people):
		date = random.randint(0, num_days-1)
		if date in birthdays: 
			same_birthday = True
			break
		birthdays.append(date)
	if same_birthday: birth_count += 1
print(birth_count / trials)

''' # 43 - birthday1.py <c> <n>, using a list for PEOPLE			43	HALF
'''
Write a program birthday2.py <c> <n> as before but use a list for the 
calendar, not the people.


import sys
import random

num_days = int(sys.argv[1])
num_people = int(sys.argv[2])
calendar = [0] * num_days
same_birthday = False

for _ in range(num_people):
	date = random.randint(0, num_days - 1)
	calendar[date] += 1
	if calendar[date] > 1: 
		same_birthday = True
		break
print(same_birthday)
''' # 44 - birthday1.py <c> <n>, using a list for CALENDAR		44	HALF
'''
Write a function polya(dna) that returns the length of the longest 
stretch of As in a dna sequence.
											45	

def polya(dna):
	max_len = 0 # set variable
	for i in range(len(dna)): # iterate through seq
		if dna[i] == 'A': # check for A
			run_len = 1 # start run_len
			for j in range(i+1, len(dna)): # check for more A
				if dna[j] == 'A': run_len += 1 # if A add to runlen
				else: break
			i = j # update i to remove unnecessary iteration
			if run_len > max_len: max_len = run_len # update maxlen
	return max_len		

print(polya('ACGTAAAACGT'))
print(polya('ACGTAAG'))
print(polya('ACGTACGTAAAAAAAAAACGT'))

''' # 45 - polya(dna)	
'''
Write a program char_count.py that prints out the character count of each character 
in a file. Invisible characters should be displayed by their ASCII value rather than 
the character. restrict quality scores to 33-126

def char_count(s):
	characters = []
	char_counts = []
	for c in s:
		if c not in characters:
			characters.append(c)
			char_counts.append(1)
		else:
			idx = characters.index(c)
			char_counts[idx] += 1
	for i in range(len(characters)):
		if ord(characters[i]) < 33 or ord(characters[i]) > 126: char = ord(characters[i])
		else: char = characters[i]
		num = char_counts[i]
		print ('Character', char, 'is counted', num, 'times')
		
print(char_count('hello world'))
print(char_count('heLlo wOrld'))

''' # 46 - char_count.py											46
'''
Write a function read_fasta(file) that reads a FASTA file and returns the 
definition line and the sequence.
''' # 47 - read_fasta - DON'T NEED FOR E3							47	N/A
'''
Write a program gc_analysis.py <fasta> <window> that computes the average GC 
composition and GC skew of a sequence in windows. The two command line arguments 
are file name and window size.


import sys

seq = sys.argv[1]
k = int(sys.argv[2])
comp_total = 0
skew_total = 0
n = 0

for i in range(0, len(seq) -k+1):
	window = seq[i:i+k]
	g = window.count('G')
	c = window.count('C')
	comp_total += (g + c) / len(seq)
	if g + c == 0: skew_total += 0
	else: skew_total += (g - c) / (g + c)
	n += 1
	
comp_avg = comp_total / n
skew_avg = skew_total / n

print('The average gc composition is', comp_avg)
print('The average gc skew is', skew_avg)

''' # 48 - gc_analysis.py 										48	DONE
'''
Write a program dust.py <fasta> <window> <threshold> that masks low complexity 
DNA sequences, replacing low entropy regions with N. Command line arguments include 
the file name, window size, and entropy threshold.

import math
import sys
import mcb185

def entropy(seq):
	pa = seq.count('A') / len(seq)
	pc = seq.count('C') / len(seq)
	pg = seq.count('G') / len(seq)
	pt = seq.count('T') / len(seq)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h
	
def dust(seq, k, t):
	mask = list(seq)
	for i in range(len(seq) -k+1):
		subseq = seq[i:i+k]
		if entropy(subseq) < t:
			for j in range(i, i+k): mask[j] = 'N'
	return ''.join(mask)

seq = sys.argv[1]
k = int(sys.argv[2])
t = float(sys.argv[3])

print(dust(seq, k, t))
''' # 49 - dust(seq, k, t)										49	DONE

