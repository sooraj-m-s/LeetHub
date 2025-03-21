# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            crnt = slow.next
            slow.next = prev
            prev = slow
            slow = crnt
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True