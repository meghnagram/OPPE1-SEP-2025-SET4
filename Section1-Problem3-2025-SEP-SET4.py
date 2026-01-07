def separate_outer_chars(s, n):
    '''
    Given a string s and an integer n, remove the first n and last n characters
    and form the tuple ('outer_chars', 'inner_chars') with
    removed outer characters joined together and the inner chars
    as elements.


    Example:
        >>> s = "programming"
        >>> n = 3
        >>> separate_outer_chars(s,n)
        ("proing", "gramm")

    Args:
        s (str): The input string.
        n (int): Number of characters to remove from both ends.

    Returns:
        str: The resulting string after removing outer characters.
    '''
    
    
    return (s[:n]+s[-n:], s[n:-n])
    

# Separate Outer Characters
# Write a function separate_outer_chars that removes n characters from both the beginning and end of a given string s and creates a tuple with two strings ('outer_chars', 'inner_chars') with the outer chars joined together as the first element and the inner chars as the second element.

# Assume the length of the string s will be greater than or equal to 2*n.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> s = "programming"
# >>> n = 3
# >>> separate_outer_chars(s,n)
# ("proing", "gramm")
# Three characters from start and end of the word programming is removed.
