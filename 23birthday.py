'''
You may have heard of the 'birthday paradox' before. Write a program that simulates the 
problem by filling up classrooms of students with randomly chosen birthdays. Make the 
number of days in the calendar and the number of people in the classroom command line 
arguments. You will have to run this thousands of times to get an accurate estimate, 
so have a parameter for the number of trials.
'''

import random
import sys

days = int(sys.argv[1])    # number of days in the calendar
people = int(sys.argv[2])  # number of people in the classroom
trials = int(sys.argv[3])  # number of trials

'''
In this program, you must use a list for the birthdays. For example, if there are 23 
people in the classroom, you will list.append() 23 times (unless you're extra-clever 
and figure out how to make a short-circuit).
'''

sames = 0
for i in range(trials):
	birthdays = []
	same_bday = False
	for i in range(people):
		bday = random.randint(0, days-1)
		if bday in birthdays: 
			sames += 1
			break
		birthdays.append(bday)

	
prob_of_same = sames/trials
print('The probability of a same birthday given', trials, 'trials is', prob_of_same)


