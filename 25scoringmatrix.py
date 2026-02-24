import sys
'''
A scoring system for aligning nucleotide sequences is often described with 2 values: 
match and mismatch. For example, +1 for match, -1 for mismatch. Printed out in a 
matrix, that would look like this:
								   A  C  G  T
								A +1 -1 -1 -1
								C -1 +1 -1 -1
								G -1 -1 +1 -1
								T -1 -1 -1 +1

Write a program that can print out a match-mismatch scoring matrix. The alphabet, match, 
and mismatch are all command line parameters. For example, the command line for 
generating the matrix above would look like this:
					 25scoringmatrix.py ACGT +1 -1
'''

seq = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('   ', end='')
for nt in seq: print(nt, end='  ')
print()

for i in range(len(seq)):
	print(seq[i], end=' ')
	for j in range(len(seq)):
		if seq[i] == seq[j]: print(mat, end=' ')
		else: 				 print(mis, end=' ')
	print()

