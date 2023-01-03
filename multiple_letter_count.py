def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # Sharon's attempt
    # all_frequency = {}
    # for i in phrase:
    # if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" :
    # all_frequency[i] +=1
    #
    # print (all_frequency)
    #

    counter = {}
    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    return counter
