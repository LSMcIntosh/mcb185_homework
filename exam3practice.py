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
''' # 41 - print_matrix.py
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
''' # 42 - Pythagorean Triples
'''
import sys
import random

num_days = int(sys.argv[1])
num_people = int(sys.argv[2])
same_birthday = False
birthdays = []

for person in range(num_people):
	date = random.randint(0, num_days-1)
	if date in birthdays: 
		same_birthday = True
		break
	birthdays.append(date)
print(same_birthday)
''' # 43 - birthday1.py <c> <n>, using a list for PEOPLE
'''
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
''' # 44 - birthday1.py <c> <n>, using a list for CALENDAR
'''
Write a function polya(dna) that returns the length of the longest 
stretch of As in a dna sequence.
''' # 45 - polya(dna)

def polya(dna):
	a_count = 0
	for i in range(len(dna)):
		if dna[i] != 'A': continue
		a_count += 1
		for j in range(i, len(dna)):
			if dna[j] != 'A': continue
			a_count += 1
	return a_count
	
print(polya('ACGTACGTAAAAAAAAAACGT'))
			
			
	
		

	