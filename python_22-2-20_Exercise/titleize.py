def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    print (phrase.title())

# I originally had the following because I didn't know title took everything else to lower case:
    # print (phrase.lower().title())
# 

