import random
	
status = "unconcious."
failure = 0
success = 0

print ("You are at 0 hit points, and you are", status)

while status == "unconcious.":
	roll = random.randint(1, 20)
	if   roll == 20: status = "revived with one hit point!"
	elif roll == 1:  failure += 2
	elif roll >= 10: success += 1
	else: 			 failure += 1
	if success == 3: status = "stable."
	if failure == 3: status = "dead :("
	print ("You rolled a", roll, "and you are", status)