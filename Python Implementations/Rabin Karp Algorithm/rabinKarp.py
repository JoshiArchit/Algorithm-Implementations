"""
Filename : rabinKarp.py
Author : Archit Joshi
Description : Implementation of the Rabin Karp algorithm to find pattern
              occurrences in a string.
              Complexity : O(n)
Language : python3
"""


def hashVal(string):
    """
    Simple has function that returns the hash value as sum of ordinal values
    for each character in the string.

    :param string: string of letters and characters
    :return: hash values for input string
    """

    hashValue = 0

    for char in string:
        hashValue += ord(char)

    return hashValue


def rabinKarp(text, pattern):
    """
    Rabin Karp function which utilises a rolling hash function to check if a
    pattern exists in a string.

    :param text: Larger string
    :param pattern: pattern to find
    :return: list of indexes where the pattern starts in the larger string,
             else -1
    """

    m = len(text)
    n = len(pattern)
    result = []

    # Get initial hash values
    text_hash = hashVal(
        text[:n])  # hash value for text with the pattern length
    pat_hash = hashVal(pattern)

    for i in range(m - n + 1):
        if text_hash == pat_hash:
            result.append(i)

        # Calculate rolling hash for text
        if i < m - n:
            text_hash = text_hash - ord(text[i]) + ord(text[i + n])

    return result


def main():
    # haystack = input("Enter string : ")
    # needle = input("Enter pattern to find : ")
    haystack = "sadbutsad"
    needle = "sad"
    result = rabinKarp(haystack, needle)
    print("String : ", haystack)
    print("Pattern : ", needle)
    if result:
        print("The pattern occurs starting at indexes : ", result)
    else:
        print("Pattern doesnt exist in the original string.")


if __name__ == "__main__":
    main()
