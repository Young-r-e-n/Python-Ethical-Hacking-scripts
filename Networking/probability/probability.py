from itertools import product

outcomes = ["1", "2", "x"]

# Generate all possible combinations of 8 games
combinations = list(product(outcomes, repeat=8))

# Calculate the number of betslips
number_of_betslips = len(combinations)

# Save the combinations to a text file
with open("betslips.txt", "w") as file:
    for combination in combinations:
        file.write(" ".join(combination) + "\n")

# Print the combinations
print("The different combinations of 8 games are:")
for combination in combinations:
    print(" ".join(combination))

print("\nThe total number of betslips is:", number_of_betslips)
