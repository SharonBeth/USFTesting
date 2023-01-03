def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # reverse = phrase[::-1]
    # reverse = reverse.replace(" ", "").lower()
    # phrase = phrase.replace(" ", "").lower()
    # 
    # if phrase == reverse:
        # print (True)
    # else: 
        # print (False)

    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]


