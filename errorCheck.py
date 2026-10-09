
def evenParity(bits):
    """
    Determine whether a bit string has even parity using the count method.

    Even parity means the string contains an even number of '1' bits.

    Parameters:
        bits: A string containing binary digits ('0' and '1'); str

    Return Value:
        True if the number of '1' bits is even, False otherwise; bool

    Examples:
        >>> evenParity('110101')
        True
        >>> evenParity('110001')
        False
    """
    pass

def evenParityNoCount(bits):
    """
    Determine whether a bit string has even parity without using count().

    Even parity means the string contains an even number of '1' bits.

    Parameters:
        bits: A string containing binary digits ('0' and '1'); str

    Return Valuee:
        True if the number of '1' bits is even, False otherwise; bool

    Examples:
        >>> evenParityNoCount('110101')
        True
        >>> evenParityNoCount('110001')
        False
    """
    pass

def makeEvenParity(bits):
    """
    Append one bit to a bit string so that the result has even parity.

    Calls evenParity() to determine which bit should be appended.

    Parameters:
        bits: A string containing binary digits ('0' and '1'); str

    Return Value:
        The original bit string with one parity bit appended; str

    Examples:
        >>> makeEvenParity('110101')
        '1101010'
        >>> makeEvenParity('110001')
        '1100011'
    """
    pass

def checksum(word):
    """
    Append a checksum character to a lowercase alphabetic string.

    Each character is converted to a value from 0 to 25, where 'a' is 0
    and 'z' is 25. The values are added, and the sum modulo 26 is
    converted back to a character and appended to the original string.

    Parameters:
        word: A string containing lowercase letters; str

    Return Value:
        The original word with its checksum character appended; str

    Examples:
        >>> checksum('snow')
        'snowp'
    """
    pass

def checksumCheck(word):
    """
    Check whether the final character of a string is a valid checksum.

    Recalculates the checksum for the string without its final character
    and compares the result with the supplied final character.

    Parameters:
        word: A lowercase alphabetic string ending with a checksum
            character; str

    Return Value:
        True if the final character is the correct checksum, False otherwise; bool

    Examples:
        >>> checksumCheck('snowp')
        True
        >>> checksumCheck('snowy')
        False
    """
    pass

def hamming(bit_seq1: str, bit_seq2: str) -> int:
    """
    Calculate the Hamming distance between two bit strings.

    The Hamming distance is the number of positions at which the two
    strings contain different bits. Both strings are assumed to have
    the same length.

    Args:
        bit_seq1 (str): The first bit string.
        bit_seq2 (str): The second bit string.

    Returns:
        int: The number of positions where the two strings differ.

    Examples:
        >>> hamming('011100110001', '011000110101')
        2
    """
    pass

