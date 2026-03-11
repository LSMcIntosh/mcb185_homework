import sys
import sequence
import mcb185
'''
A much more efficient algorithm only counts the initial window. After that, it "moves" 
the window by dropping off one nucleotide on the left and adding one on the right.

Re-write 34skew.py using the more efficient algorithm and then calculate GC-skew and 
GC composition in 1000 nt windows in the E.coli genome.

For debugging purposes you might find it very useful to write the program twice: once 
using the wasteful strategy and once using the faster algorithm. When making performance 
optimizations it's easy to make mistakes. Having a simpler solution helps debug the more 
difficult problem.

If you're so inclined, try timing the simple and fast algorithms with the time program. 
Use various window sizes to see how much that affects compute time. Your command line 
might look like the following. Here, it is assumed your program takes 2 arguments: the 
window size (1000) and a soft-linked fasta file (because the original name is so long).
		time python3 34skew.py ecoli.fa.gz 1000

'''
k = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	name = defline
	first = seq[0:k]
	g = first.count('G')
	c = first.count('C')
	for i in range(len(seq) -k+1):
		off = seq[i]
		on = seq[i+k]
		if   off == 'G': g -= 1
		elif off == 'C': c -= 1
		if   on == 'G': g += 1
		elif on == 'C': c += 1
		gc_comp = (g + c) / k
		if g + c == 0: gc_skew = 0
		else: gc_skew = (g - c) / (g + c)
		print(gc_comp, gc_skew)
