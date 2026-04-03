# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find midpoint with slow-fast pointers
        
        # Loop from midpoint till end and reverse direction of links
        # Use fast pointer as right
        # Left at head
        # While left != right
            # Add left to reordered linked list
            # Store left next in temp var
            # Add right as next of left
            # Move left pointer to temp
            # Move right to next node

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse direction of second part of list
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge two halves of list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

        

        

        