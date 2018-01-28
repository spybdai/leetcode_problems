"""
todo: get better performance
"""


def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """

    max_len = 0

    index = 0
    start = ''

    while index < len(s):
        sub1, sub2 = split_string(start, s[index])

        max_len = max(max_len, len(sub1), len(sub2))

        start = sub2

        index += 1

    return max_len


def split_string(s, c):
    index = s.find(c)

    if index == -1:
        return '', s + c

    adjust_index = index + 1

    return s[:adjust_index], s[adjust_index:] + c