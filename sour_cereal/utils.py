def to_camel_case(string: str) -> str:
    '''Formats a string to camel case.

    :param string: the string to be formatted
    :type string: str
    :return: a camel case string
    :rtype: str
    '''
    return ''.join((word[0].upper() + word[1:] for word in string.split('_')))
