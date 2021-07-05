def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    c_letter = to_swap.upper()
    l_letter = to_swap.lower()
    res=''

    for letter in phrase:
        if letter == c_letter:
            res += letter.lower()
        elif letter == l_letter:
            res += letter.upper()
        else:
            res+=letter
    
    return res

