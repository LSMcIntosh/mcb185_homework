'''
There are a few comment lines at the top of the file. The other lines describe genes 
and other features. We examined this file with cut and uniq way back in unit 1.

Create a program called 31cdslength.py that reports the lengths of protein-coding 
genes in the E. coli genome. The program will need to perform the following tasks 
as it reads each line of the file.

 - Skip over comment lines
 - Find CDS features (or skip over all non-CDS features)
 - Extract the begin and end coordinates
 - Convert the coordinates to integers
 - Report the length of the CDS (end - begin + 1)
 - Type the following lines and observe how the code works. 
   Delete it all and re-write it from a blank page.

''' # Description
import gzip
import sys
'''
with gzip.open(sys.argv[1], 'rt') as fp: # opens file
	for line in fp: # iterates through lines
		if line[0] != "#": # checks to see if the line is a comment
			words = line.split() # splits string into substrings
			if words[2] == 'CDS': # checks for data type
				beg = int(words[3]) # gets beginning value
				end = int(words[4]) # gets ending value
				print(end - beg + 1) # returns value difference?
''' # reference (first attempt)


with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] == 'CDS':
				beg = int(words[3])
				end = int(words[4])
				length = end - beg + 1
				print(length)
				
			