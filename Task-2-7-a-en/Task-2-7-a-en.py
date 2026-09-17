# Reading input data
a = input("Enter the current code: ").strip()  # Input current code
b = input("Enter the target code: ").strip()  # Input target code
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
print(f"Current code: {a}")
print(f"Target code: {b}")
print(f"Minimum number of moves: {total_moves}")
