def replace_spaces_with_index(s):
    '''
    Given a string s, replace each space (' ') with its index position in the string.

    Example:
        >>> replace_spaces_with_index("a b c")
        'a2b3c'

    Args:
        s (str): Input string.

    Returns:
        str: A new string where each space is replaced with its index.
    '''
    
    
    result = ''
    for i, ch in enumerate(s):
        if ch == ' ':
            result += str(i)
        else:
            result += ch
    return result
    

# Replace Spaces with Index
# Write a function that replaces every space ' ' in a given string with its index position in the string.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> replace_spaces_with_index("a b c")
# 'a2b3c'
