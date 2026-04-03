# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        # Move fast pointer first
        for _ in range(n-1):
            fast = fast.next

        prev = None

        # Move fast/slow pointers same rate
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next

        # Pop out the node at slow
        if prev is None:
            # We must be removing the head
            head = slow.next
        else:
            prev.next = slow.next

        return head