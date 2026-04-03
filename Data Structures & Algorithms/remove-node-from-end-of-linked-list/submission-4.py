# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head

        # Move fast pointer first
        for _ in range(n):
            fast = fast.next

        dummy = ListNode(-1, head)
        slow = dummy

        # Move fast/slow pointers same rate
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove that node after slow
        slow.next = slow.next.next

        return dummy.next