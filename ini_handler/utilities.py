"""A collection of regularly used functions"""


def validate_key_type(key):
    """Checks if the key is of type str.

    Args:
        key(str): the key to validate"""
    if not type(key) == str:
        raise TypeError('Key must be of type string')
