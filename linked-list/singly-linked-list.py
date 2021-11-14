class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.cursor = self.head
    
    def get(self, index: int) -> int:
        self.cursor = self.head

        for i in range(index):
            if self.cursor != None:
                self.cursor = self.cursor.next

        return self.cursor.value if self.cursor != None else -1

    def addAtHead(self, value: int) -> None:
        node = ListNode(value, self.head)
        self.head = node
        self.cursor = self.head
        return None
    
    def addAtTail(self, value: int) -> None:
        if self.head == None:
            self.addAtHead(value)
            return None

        while self.cursor != None:
            previous = self.cursor
            self.cursor = self.cursor.next
        
        node = ListNode(value)
        previous.next = node
        self.cursor = node

        return None
    
    def addAtIndex(self, index: int, value: int) -> None:
        if index == 0:
            self.addAtHead(value)
            return None
        
        self.cursor = self.head

        for i in range(index - 1):
            if self.cursor != None:
                self.cursor = self.cursor.next

        if self.cursor == None:
            return None

        prev = self.cursor
        next = self.cursor.next

        node = ListNode(value, next)
        prev.next = node

        return None
    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return None

        if index == 0:
            self.head = self.head.next
            return None

        self.cursor = self.head

        for i in range(index - 1):
            if self.cursor != None:
                self.cursor = self.cursor.next

        if self.cursor == None:
            return None
        
        # Here is some error
        next = self.cursor.next.next
        self.cursor.next = next

        return None
    
    def listAll(self):
        self.cursor = self.head

        while self.cursor != None:
            print(self.cursor.value)
            self.cursor = self.cursor.next


numbers = SinglyLinkedList()
numbers.addAtTail(0)
numbers.addAtTail(1)
numbers.addAtTail(2)
numbers.deleteAtIndex(-1)

numbers.listAll()