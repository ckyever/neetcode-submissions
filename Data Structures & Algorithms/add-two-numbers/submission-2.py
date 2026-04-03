# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node, l2_node = l1, l2
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1_node or l2_node:
            l1_num = l1_node.val if l1_node else 0
            l2_num = l2_node.val if l2_node else 0
            sum = l1_num + l2_num + carry
            carry = sum // 10
            tail.next = ListNode(sum % 10)
            tail = tail.next

            if l1_node:
                l1_node = l1_node.next
            
            if l2_node:
                l2_node = l2_node.next
        
        if carry > 0:
            tail.next = ListNode(carry)
        
        return dummy.next
