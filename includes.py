def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # String 
        # .find() returns -1 if x is not found in string

    # list 
        # .count()  Returns the number of elements with the specified value 
    #   or.index()  Returns the index of the first element with the specified value

    # tuple
        # .index()  Searches the tuple for a specified value and returns the position of where it was found
        # .count()  Returns the number of times a specified value occurs in a tuple

    # dictionary
        # .get()    This returns the value of the key if present, if not it returns as None
    # set
        # Must loop through, also no index number, because sets are not numbered


    # if type(collection) == list:
        # if collection.count(sought) > start:
            # return True
    # if type(collection) == str:
        # if collection.find(sought) > start:
            # return True
    # if type (collection) == tuple:
        # if collection.index(sought) > start:
            # return True
    # if type(collection) == dict:
        # if collection.get(sought) != None:
            # return True
    # if type(collection) == set:
        # set_indicator ={True for each in collection if each == sought}
        # if set_indicator == True:
            # print (True)
    # return False
    if isinstance(collection, dict):
        return sought in collection.values()
    if start is None or isinstance(collection, set):
        return sought in collection
    return sought in collection[start:]       

# string  if NOT -1 True
# list    if NOT <0 True  (need to double check return if not existant)
# tuple   if not 0    True    (need to double check return if not existant)
# dictionary if Not = None true
# set     must loop through
# 
