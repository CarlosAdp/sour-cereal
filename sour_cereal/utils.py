def to_camel_case(string: str) -> str:
    return ''.join((word[0].upper() + word[1:] for word in string.split('_')))
