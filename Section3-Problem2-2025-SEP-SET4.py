


n = int(input())
total = 0
inside = False
for i in range(n):
    for char in input():
        if char == '[':
            inside = True
            num = ""
            continue
        if inside:
            if char == ']':
                inside = False
                total += int(num)
                continue
            else:
                num+=char
print(total)


# Sum Numbers Inside Square Brackets
# Given a multiline text, extract all numbers that appear inside square brackets in the whole text, compute their sum, and output this sum.

# There will be only valid integers inside the square brackets (including negative).
# There will be no nested brackets and there will be always closing bracket in the same line.
# The brackets might span over multiple line(beginning in one line and ending in another).
# There may be other characters (including other brackets) outside the numeric brackets – ignore them.
# Input Format

# n
# line_1
# line_2
# ...
# line_L
# The first line contains a single integer n – the number of following lines.
# Each of the next n lines is an arbitrary string that may contain zero or more integer numbers enclosed in square brackets [ and ].
# Output Format A single integer – the sum of all numbers found inside [ ].

# Example

# Input

# 4
# The price is [12] dollars.
# No brackets here.
# Multiple [3][4][5] in one line.
# [100] is the final one.
# Output

# 124
# Explanation

# Numbers extracted: 12, 3, 4, 5, 100 → sum = 124.
