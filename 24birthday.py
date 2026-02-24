'''
This is the same problem as above, but instead of making a list of birthdays (e.g. 23) 
make a list from the calendar (e.g. 365). In the previous program, you appended 
birthdays to a list. In this one, all possible days are already in a list, so assigning 
a birthday is: calendar[birthday] += 1.

Another way to think about this problem is to imagine you're throwing darts at a 
calendar. A shared birthday is when 2 darts hit the same day.
'''
import sys
import random

days = int(sys.argv[1])
people = int(sys.argv[2])
trials = int(sys.argv[3])

sames = 0
for i in range(trials):
	calendar = [0]*days
	same_birthday = False
	for person in range(people):
		bday = random.randint(0, days-1)
		if calendar[bday] >= 1:
			sames += 1
			break
		calendar[bday] += 1

bdayprob = sames/trials
print('The probability of a shared birthday given', trials, 'trials is:', bdayprob)



