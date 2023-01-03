def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # If we are supposed to figure out to import a library, then the following is my answer:

    # import statistics

    # print(statistics.mode(nums))

    # if we are not supposed to use a library:

    counts = {} 
    # The above variable  makes an empty dictionary.

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    max_value = max(counts.values())

    for (num, freq) in counts.items():
        if freq == max_value:
            return num 
