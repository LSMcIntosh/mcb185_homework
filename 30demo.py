import math
import argparse
import sys
import random
import mcb185
''' Demo, practice, and in-class notes for Unit 3'''
# Notes 3/3 
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
	if seq[i] == 'A': # start with first IDed 'A'
		run_start = i
		run_len = 1
		for j in range(i+1, len(seq)): # sequence though nt after 'A'
			if seq[j] == 'A': run_len += 1 # add if more 'A' break if not
			else: break
		i = j
		print(run_start, run_len)
		#if run_len > max_run: 
		#	max_run = run_len
		#	max_pos = run_start
	i  += 1
''' # E3Q45 polyA
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
''' # fizzprime with grep
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
''' # really inefficient entropy calc (mine)
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
''' # crazycase test question
'''
# stats function exactly as I wrote it on the test:
def stats(X):
	X.sort()
	n = len(X)
	midpoint = n//2
	tot1 = 0
	for val in X: tot1 += val
	mean = tot1/n
	tot2 = 0
	for val in X: tot2 += (val/mean)**2
	stdev = (tot2/n)**(0.5)
	if len(X) % 2 == 1: median = X[midpoint]
	else: median = (X[midpoint] + X[midpoint + 1])/2
	return mean, stdev, median
	
X = [1, 2, 3, 4, 5]
res = stats(X)
print(res[0], res[1], res[2])
''' # stats test question
# Notes 3/5
'''
def practice1():
	for a in range(1, 15):
		for b in range(a+1, 15):
			c = (a**2 + b**2)**(0.5)
			if c % 1 != 0: continue
			print(a, b, c)

# 42: Triples
def triples():
	stuff = ('A', 'B', 'C', 'D')
	for i in range(len(stuff)):
		for j in range(i+1, len(stuff)):
			print(stuff[i], stuff[j])
''' # 42: Triples
'''
cal = int(sys.argv[1])
num = int(sys.argv[2])

shared_birthdays = 0
rounds = 50
for g in range(rounds):
	shared = False
	birthdays = []
	for _ in range(num):
		birthdays.append(random.randint(0, cal-1))
	for i in range(num):
		for j in range(i+1, num):
			if birthdays[i] == birthdays[j]:
			shared = True
	if shared: shared_birthdays += 1		
print(shared_birthdays/rounds)
''' # 43 Birthday paradox 1				
'''
cal = int(sys.argv[1]) # days in the year
num = int(sys.argv[2]) # number of people

shared = False
calendar = [0] * cal
for _ in range(num):
	day = random.randint(0, cal-1)
	calendar[day] += 1
for date in range(cal):
	if calendar[date] > 1: shared = True
if shared: print('hooray')
else:	   print('not this time')
''' # 44 Birthday paradox 2
'''
def char_count1():
	s =  'hello	this is fun!'
	characters = []
	char_count = []
	#print(char_count(s))
	for c in s:
		if c not in characters:
			print('first time seeing', c)
			characters.append(c)
			char_count.append(1)
		else:
		print('seen', c, )
			idx = characters.index(c)
			char_count[idx] += 1
			
def char_count2(s):
	chars = [0] * 128
	for c in s:
		chars[ord(c)] += 1
	for i in range(len(chars)):
		if chars[i] == 0: continue
		print(ascii(i), chars[i])

# if ord(char[i]) outside of visible range (33, 126) it is invisible (0-32, 127+)

''' # 46 char_count
''' 
# import argparse

seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
hard = 'ACGTACGTNNNNNNNNNNNCGTACGT'
def entropy(seq):
	pa = seq.count('A')/len(seq)
	pc = seq.count('C')/len(seq)
	pg = seq.count('G')/len(seq)
	pt = seq.count('T')/len(seq)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h

parser = argparse.ArgumentParser()
parser.add_argument('fasta')
parser.add_argument('-window', type=int, default=11)
parser.add_argument('--threshold', type=float, default=1.1)
parser.add_argumet('--wrap') ???
parser.add_argument('--hard', action='store_true', help='perform hard masking, soft is default')
arg = parser.parse_args()

k = arg.window
t = arg.threshold
for defline, seq in mcb185.read_fasta(arg.fasta)

	mask = list(seq)
	for i in range(len(seq) -k+1):
		if entropy(seq[i:i+k]) > t: continue
		for j in range(i, i+k):	
			if arg.hardL mask[j] = 'N'
			else: mask[j] = seq[j].lower()
	print('<', defline, sep='', )
	seq = ''.join(mask)
	for i in range(0, len(seq), arg.wrap):
		print(seq[i:i+arg.wrap])
		
in CL: python3 programname.py ~/Code/MCB185/data/C.elegans
''' # 49 dust (again)
# Notes 3/10
'''
# use a list for the PEOPLE, not the calender
# import sys
# import random
num_days = int(sys.argv[1])
num_people = int(sys.argv[2])
birthdays = list()
same_birthday = False

# get all birthdays into a list
for _ in range(num_people):
	date = random.randint(0, num_days - 1)
	if date in birthdays:
		same_birthday = True
		break
	birthdays.append(date)
print(same_birthday)
''' # 43 practice
'''
# use a list for the CALENDAR, not the people
# import sys
# import random
num_days = int(sys.argv[1])
num_people = int(sys.argv[2])

# make an empty calendar
calendar = [0] * num_days

# fill calendar with dates and check as you go
same_birthday = False
for _ in range(num_people):
	date = random.randint(0, num_days - 1)
	if calendar[date] != 0: 
		same_birthday = True
		break
	calendar[date] += 1
print(same_birthday)

# check cal for shared birthdays
# found = False
# for birthday_count in calendar:
#     if birthday_count > 1: found = True
''' # 44 practice
'''
 # with command line arguments <alphabet> <plus> <minus>
 
alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('   ', end='')
for let in alph: print(let, end='  ')
print()
for i in range(len(alph)):
	print(alph[i], end=' ')
	for j in range(len(alph)):
		if alph[i] == alph[j]: print(mat, end=' ')
		else:				   print(mis, end=' ')
	print()

def another(alph, mat, mis):
	print('   ', end='')
	for nt in alph: print(nt, end='  ')
	print()
	for nt1 in alph:
		print(nt1, end=' ')
		for nt2 in alph:
			if nt1 == nt2: print(mat, end=' ')
			else:		   print(mis, end=' ')
		print() # with nt1/2 in alph instead of for i/j in range()
''' # 41 practice (matrix)
'''
seq = 'ACGTAAAAAAACGT'

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

def dust(seq, w, t):
	eseq = list(seq)
	for i in range(len(seq) -w+1):
		win = seq[i:i+w]
		if entropy(win) < t:
			for j in range(i, i+w):
				eseq[j] = 'N' # we edit the list, NOT the seq
				# soft: eseq[j] = seq[j].lower()
	return ''.join(eseq)
''' # 49 practice (function) GUARENTEED ON THE EXAM
'''
# on exam, import sys
# CLI = python3 gc_analysis.py ATATACAAATTACGAT 7
seq = sys.argv[1]
k = int(sys.argv[2])
for i in range(len(seq) -k+1):
	subseq = seq[i:i+k]
	c = subseq.count('C')
	g = subseq.count('G')
	gc_comp = (c + g) / len(subseq)
	if g + c == 0: gc_skew = 0
	else:		   gc_skew = (g - c) / (g + c)
	# OR gc_skew = (g - c) / (g + c) if g+c != 0 else 0

# calendar = [x for x in rangex] ??? python-ism
''' # 48 practice
'''

seq = sys.argv[1]
k = int(sys.argv[2])
first = seq[0:k]
g = first.count('G')
c = first.count('C')
for i in range(len(seq) -k+1):
	off = seq[i]
	on = seq[i+k]
	if   off == 'C': c -=1
	elif off == 'G': g -= 1
	if   on == 'C': c += 1
	elif on == 'G': g += 1
	gc_comp = (g + c) / len(seq)
	if g + c == 0: gc_skew = 0
	else:		   gc_skew = (g - c) / (g + c)
# what do I do with this?? report/print every iteration?? or how do I get
# one value
'''# windowing: add and drop
'''
Any resources for learning more bioinformatics 

rosalind.io - programming puzzles
bioinformatics research
	- get into a lab

compare tools and their effectiveness??
like sequence aligners

can you replicate an experiment??
find out what programs work best under what circumstances

be able to install other people's software and organize the files

    - for the first 30 nt, I’m looking for an average KD >= 2.5 over a window size of 8 nt
    - for the rest of the seq I’m looking for a window size of 11 with an average KD >. 2
    - AND that the window doesn’t contain proline
''' # 3/11/26 OH Notes

