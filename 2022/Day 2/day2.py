openinput = open('input.txt') # Open text file containing strategy guide.
strategy = openinput.read().splitlines() # Copy file contents to variable, split by lines.
openinput.close() # Close text file.

#Variables Setup Part 1 and 2
score = 0
A = 1 # Opponent's Rock score
B = 2 # Opponent's Paper score
C = 3 # Opponent's Scissors score
X = 1 # My Rock score
Y = 2 # My Paper score
Z = 3 # My Scissors score
win = 6 # Win Score
draw = 3 # Draw Score
lose = 0 # Lose Score

#Variables Setup Part 2
score2 = 0
X2 = lose
Y2 = draw
Z2 = win

for i in range(0, len(strategy)): # For Part 1.
	opponent, me = strategy[i].split() # Split the input of two values to two variables. 

	if me == "X" and opponent == "C": # Rock beats Scissors
		score += X + win

	if me == "X" and opponent == "A": # Rock draws Rock
		score += X + draw

	if me == "X" and opponent == "B": # Rock loses Paper
		score += X + lose

	if me == "Y" and opponent == "A": # Paper beats Rock
		score += Y + win

	if me == "Y" and opponent == "B": # Paper draws Paper
		score += Y + draw

	if me == "Y" and opponent == "C": # Paper loses Scissors
		score += Y + lose

	if me == "Z" and opponent == "B": # Scissors beats Paper
		score += Z + win

	if me == "Z" and opponent == "C": # Scissors draws Scissors
		score += Z + draw

	if me == "Z" and opponent == "A": # Scissors loses Rock
		score += Z + lose

for i in range(0, len(strategy)): # For Part 2.
	opponent, me = strategy[i].split() # Split the input of two values to two variables. 

	if me == "X" and opponent == "C": # Lose
		score2 += X2 + Y

	if me == "X" and opponent == "A":
		score2 += X2 + Z

	if me == "X" and opponent == "B":
		score2 += X2 + X

	if me == "Y" and opponent == "A": # Draw
		score2 += Y2 + X

	if me == "Y" and opponent == "B":
		score2 += Y2 + Y

	if me == "Y" and opponent == "C":
		score2 += Y2 + Z

	if me == "Z" and opponent == "B": # Win
		score2 += Z2 + Z

	if me == "Z" and opponent == "C":
		score2 += Z2 + X

	if me == "Z" and opponent == "A":
		score2 += Z2 + Y

#Part 1
print(score)

#Part 2
print(score2)