def is_palindrome(text):
    """Checks if a string is a palindrome.

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    text = text.lower()  
    return text == text[::-1]  


print(is_palindrome("aca"))    
print(is_palindrome("aabbaa")) 
print(is_palindrome("abbbb"))  
print(is_palindrome("baabbb")) 
