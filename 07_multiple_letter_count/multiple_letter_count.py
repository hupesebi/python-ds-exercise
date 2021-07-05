def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    result ={}
    phrase_list = list(phrase)
    for letter in phrase_list:
        num = phrase.count(letter)
        result[letter] = num
    return result