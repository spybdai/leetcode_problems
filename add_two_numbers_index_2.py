"""
https://leetcode.com/problems/add-two-numbers/description/

Key point:
singly linked list
"""


class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode

    key point:
    handle carry carefully
    """

    start = result = ListNode(0)
    carry = 0

    while l1 and l2:

        res, carry = sum_adjust(l1.val, l2.val, carry)

        res = ListNode(res)
        result.next = res
        result = res

        l1 = l1.next
        l2 = l2.next

    # adjust l1
    while l1:

        if carry == 0:
            result.next = l1
            break

        res, carry = sum_adjust(l1.val, 0, carry)

        res = ListNode(res)
        result.next = res
        result = res

        l1 = l1.next

    # adjust l2
    while l2:

        if carry == 0:
            result.next = l2
            break

        res, carry = sum_adjust(l2.val, 0, carry)

        res = ListNode(res)
        result.next = res
        result = res

        l2 = l2.next

    # adjust carry
    if carry == 1:
        result.next = ListNode(1)

    return start.next


def sum_adjust(num1, num2, carry, base=10):

    res = num1 + num2 + carry
    carry = 0

    if res >= base:
        res %= base
        carry = 1

    return res, carry

