from string import ascii_lowercase, ascii_uppercase

openinput = open('input.txt') # Open text file containing rucksacks.
rucksacks = openinput.read().splitlines() # Copy file contents to variable, split by lines.
openinput.close() # Close text file.

total = 0

for i in range(0, len(rucksacks)): 
	halves = len(rucksacks[i])//2 # Split each rucksack to halves and assign to two variables.
	half1 = rucksacks[i][:halves]
	half2 = rucksacks[i][halves:]

	common = [rucksacks[i] for rucksacks[i] in half1 if rucksacks[i] in half2][0] # Return each item in rucksacks in common between the halves. Grab value from list.

	for i in common:
		if i in ascii_lowercase:
			total += ascii_lowercase.index(i) + 1 # Find the index position value of lowercase item and add 1 to it (26 letters in the alphabet). Add to total.
		if i in ascii_uppercase:
			total += ascii_uppercase.index(i) + 27 # Find the index position value of uppercase item and add 27 to it (26 letters in the alphabet). Add to total.

# Part 1
print(total)

openinput = open('input.txt') # Open text file containing rucksacks.
rucksacks2 = openinput.read().splitlines() # Copy file contents to variable, split by lines. Part 2
openinput.close() # Close text file.

total2 = 0

for i in range(0, len(rucksacks2), 3): # 3 step increment
	groups = rucksacks2[i: i + 3] # Return item group, every 3 items.

	commongroups = [rucksacks2[i] for rucksacks2[i] in groups[0] if rucksacks2[i] in groups[1] and rucksacks2[i] in groups[2]][0] # Return each item in rucksacks in common between the groups. Grab value from list.

	for i in commongroups:
		if i in ascii_lowercase:
			total2 += ascii_lowercase.index(i) + 1 # Find the index position value of lowercase item and add 1 to it (26 letters in the alphabet). Add to total.
		if i in ascii_uppercase:
			total2 += ascii_uppercase.index(i) + 27 # Find the index position value of uppercase item and add 27 to it (26 letters in the alphabet). Add to total.

# Part 2
print(total2)