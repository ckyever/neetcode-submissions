# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        merged_head = None
        list1_pointer, list2_pointer = list1, list2

        # Add head node
        if list2_pointer is None or list1_pointer.val <= list2_pointer.val:
            merged_head = ListNode(list1_pointer.val)
            list1_pointer = list1_pointer.next
        else:
            merged_head = ListNode(list2_pointer.val)
            list2_pointer = list2_pointer.next   

        merged_tail = merged_head
        while list1_pointer or list2_pointer:
            if list1_pointer and not list2_pointer:
                print("cky1")
                merged_tail.next = ListNode(list1_pointer.val)
                merged_tail = merged_tail.next
                list1_pointer = list1_pointer.next

            elif list2_pointer and not list1_pointer:
                print("cky2")
                merged_tail.next = ListNode(list2_pointer.val)
                merged_tail = merged_tail.next
                list2_pointer = list2_pointer.next

            elif list1_pointer.val <= list2_pointer.val:
                print("cky3")
                merged_tail.next = ListNode(list1_pointer.val)
                merged_tail = merged_tail.next
                list1_pointer = list1_pointer.next
            
            else:
                print("cky4")
                merged_tail.next = ListNode(list2_pointer.val)
                merged_tail = merged_tail.next
                list2_pointer = list2_pointer.next

        return merged_head