
def bold_nth_character(text: str, n: int) -> str:
    '''
    Returns a string where the nth character is wrapped in <b></b> tags.
    If n is invalid, returns the original string unchanged.
    '''
    
    
    if n < 1 or n > len(text):
        return text
    return text[:n-1] + "<b>" + text[n-1] + "</b>" + text[n:]
    

# Bold Nth Character
# Write a function bold_nth_character(text: str, n: int) -> str that takes a string text and an integer n as input.

# The function should return a new string where the nth character (using 1-based indexing) is wrapped with an HTML <b> tag — i.e., <b>char</b>.

# If:

# n is less than 1, or
# n is greater than the length of the string,
# then return the original string unchanged.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example:

# >>> bold_nth_character("mango", 2)
# "m<b>a</b>ngo"
# Explanation:
# The 2nd character is 'a'. Wrapping it gives "m<b>a</b>ngo".
