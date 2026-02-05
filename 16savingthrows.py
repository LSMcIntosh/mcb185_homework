import random

r1 = random.randint(1, 20)

passed = "You passed the"
failed = "You did not pass the"

if r1 >=  5: dc5  = passed
else: dc5 = failed
if r1 >= 10: dc10 = passed
else: dc10 = failed
if r1 >= 15: dc15 = passed
else: dc15 = failed

print ("You rolled a " + str(r1) + "!")
print (dc5, "DC 5 saving throw.")
print (dc10, "DC 10 saving throw.")
print (dc15, "DC 15 saving throw.")


