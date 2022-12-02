openinput = open('input.txt') # Open text file containing calories amounts.
calories = openinput.read().split("\n\n") # Copy file contents to variable, splitting by empty lines.
openinput.close() # Close text file.

for i in range(0, len(calories)):
	calories[i] = list(map(int, calories[i].splitlines())) # Using map to convert string to integer. Split items by line breaks.
	calories[i] = sum(calories[i]) # Sum list of lists of calories

calories = sorted(calories, reverse=True) # Sort results in descending order.

# Part 1
print(calories[0]) # Print top result.

# Part 2
print(sum(calories[0:3])) # Print and sum top 3 results.