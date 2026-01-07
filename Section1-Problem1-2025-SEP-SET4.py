
def is_divisible_by_last_two_digits(num: int):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by both last two digits, False otherwise.
    """
    
    
    a,b = str(num)[-2:]
    a, b = int(a), int(b)
    return a!=0 and b!=0 and num % a == 0 and num % b == 0
    

# Check Divisibility by Last Two Digits
# Write a function that checks whether a given number is divisible by both of its last two digits.

# Return False if any of the last two digits is zero.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Input: A positive integer num with at least two digits.
# Output: True if the number is divisible by both of its last two digits, otherwise False.
# Examples

# 1236 -> True, 1236 is divisible by both 3 and 6.
# 345 -> False, 345 is divisible by 5 but not divisible by 4.
# 748 -> False, 748 is divisible by 4 but not divisble by 8.
# 740 -> False, the last digit is 0.
