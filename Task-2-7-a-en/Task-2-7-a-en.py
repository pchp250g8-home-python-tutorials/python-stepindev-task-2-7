# Reading input data
a = input("Enter the current code: ")  # Input current code
b = input("Enter the target code: ")  # Input target code
a = a.strip()  # Remove useless spaces
b = b.strip()  # Remove useless spaces
n_len1 = len(a)  # Calculate the length of the 1-st string
n_len2 = len(b)  # Calculate the length of the 2-nd string
# Check if the lengths of the current and target codes match
# If the length of the current code does not equal the
# length of the target code
# and both codes are not four-digit numbers,
# the program terminates.
if (n_len1 != 4) or (n_len2 != 4) or (n_len1 != n_len2):
    print("The combination lock code must be 4 digits long.")
    print("The current and target codes must be of the same length.")
    exit()
# Calculating the minimum number of moves
total_moves = 0  # Move counter
for x, y in zip(a, b):
    # Digit difference, forward dial movement
    diff1 = abs(int(x) - int(y))
    # Digit difference, reverse dial movement
    diff2 = 10 - abs(int(x) - int(y))
    # The minimum number of moves is the difference between each digit
    # of the target code and the current safe lock code
    total_moves += min(diff1, diff2)  # Total moves – the answer
# Print information to screen
print(f"Current code: {a}")
print(f"Target code: {b}")
print(f"Minimum number of moves: {total_moves}")
