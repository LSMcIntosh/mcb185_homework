import mcb185
import sys

def hydropathy(pro):
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
	total = 0
	for aa in pro:
		ind = pro.index(aa) # find the location of the aa with list.index()
		total += kdh[ind] # find the corresponding value with the index
	avgkdh = total/len(pro) # find the average
	return avgkdh # calculating avgKDh (Exam 2 Question 35)

def hah(seq, w, t):
	kdh = False
	for i in range(len(seq) -w +1):
		window = seq[i:i+w]
		if hydropathy(window) >= t and 'P' not in window: kdh = True
	return kdh

for defline, protein in mcb185.read_fasta(sys.argv[1]):
	nterm = protein[:30]
	cterm = protein[30:]
	sigpep = hah(nterm, 8, 2.5)
	transmem = hah(cterm, 11, 2.0)
	if sigpep == False: continue 
	if transmem == False: continue
	print(defline)


