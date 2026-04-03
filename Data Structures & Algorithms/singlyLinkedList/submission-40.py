class ListNode:
    def __init__(self, value: int, nextNode = None):
        self.value = value
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current_node = self.head.next
        i = 0
        while current_node:
            if i == index:
                return current_node.value
            i += 1
            current_node = current_node.next
        return -1   

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            # If list was originally empty (only contained dummy node)
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current_node = self.head
        i = 0
        while i < index and current_node:
            i += 1
            current_node = current_node.next

        if current_node and current_node.next:
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current_node = self.head.next
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        return values
