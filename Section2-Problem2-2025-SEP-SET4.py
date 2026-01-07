


n = int(input())
c = 0
for _ in range(n):
    a,b = map(int,input().split())
    c = max(0,a+b+c-100)
    print(c)


# Add Pairs with Carry Over Above 100
# You will be given an integer n, followed by n pairs of numbers (a and b), each on its own line.

# Start with a carry value of 0.

# For each pair:

# Compute the sum of a,b and current carry
# If the sum goes above 100, the carry becomes sum - 100 else 0
# Print the resulting carry after each step.
# Use the carry from each step when processing the next line.

# NOTE:
# This is an I/O type question -- you must write the complete code to read input and print the output.

# Input Format
# n
# a1 b1
# a2 b2
# ...
# an bn
# Output Format
# Print n lines. The i‑th line should contain the carry produced after processing the i‑th pair (as described above).

# Example
# Input

# 5
# 30 40
# 80 30
# 10 90
# 90 15
# 5 5
# Processing

# 30 + 40 + 0 = 70 → ≤100 → carry = 0 → print 0
# 80 + 30 + 0 = 110 → >100 → carry = 110‑100 = 10 → print 10
# 10 + 90 + 10 = 110 → >100 → carry = 0 → print 10
# 90 + 15 + 10 = 115 → >100 → carry = 5 → print 15
# 5 + 5 + 15 = 25 → ≤100 → carry = 0 → print 0
# Output

# 0
# 10
# 10
# 15
# 0
