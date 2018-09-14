import json


def format_dictionary(dct, indent=4):
    """Formats a dictionary to be printed
    Args:
        dct (dict): Dictionary.
        indent (int): Indentation value.
    Returns:
        result (str): Formatted dictionary ready to be printed
    Examples:
        >>> dct = {'bkey':1, 'akey':2}
        >>> print(format_dictionary(dct))
        {
            "akey": 2,
            "bkey": 1
        }

    """
    return json.dumps(dct, indent=indent, sort_keys=True)


def format_float_as_string():
    """Example of formatting a float as a string
    Examples:
        >>> format_float_as_string()
        'num=0.12'
    """
    return "num={:0.2f}".format(0.123456)
