# --coding:utf-8--

# Data input: target code and current code
# Entered as four-digit numbers
a = int(input("Enter the current code: "))
m = 0  # Number of digits in the target code
b = int(input("Enter the target code: "))
n = 0  # Number of digits in the current code
total_moves = 0
a1 = a
b1 = b
# Count digits in the current code
while (a1 > 0):
    m += 1
    a1 //= 10
# Count digits in the target code
while (b1 > 0):
    n += 1
    b1 //= 10
# Check if the lengths of the current and target codes match
# If the length of the current code does not equal the
# length of the target code
# and both codes are not four-digit numbers,
# the program terminates.
if (m != 4) or (n != 4) or (m != n):
    print("The combination lock code must be 4 digits long.")
    print("The current and target codes must be of the same length.")
    exit()
a1 = a
b1 = b
# Iterate through the digits of the current and target codes
while (a1 > 0) and (b1 > 0):
    d1 = a1 % 10  # Digit of the current code
    d2 = b1 % 10  # Digit of the target code
    diff1 = abs(d1 - d2)  # Digit difference, forward dial movement
    diff2 = 10 - abs(d1 - d2)  # Digit difference, reverse dial movement
    # Minimum number of moves — the difference between each digit
    # in the target code and the current safe lock code
    total_moves += min(diff1, diff2)
    a1 //= 10  # Move to the next digit of the current code
    b1 //= 10  # Move to the next digit of the target code
# Print information to screen
print(f"Current code: {a}")
print(f"Target code: {b}")
print(f"Minimum number of moves: {total_moves}")
