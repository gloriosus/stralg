class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.cursor = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            self.cursor = None
            return -1
           
        self.cursor = self.head

        for i in range(index):
            if self.cursor != None:
                self.cursor = self.cursor.next

        return self.cursor.value if self.cursor != None else -1

    def push(self, value: int) -> None:
        node = ListNode(value, self.head)
        self.head = node
        self.cursor = self.head
        return None
    
    def append(self, value: int) -> None:
        if self.head == None:
            self.push(value)
            return None

        while self.cursor != None:
            previous = self.cursor
            self.cursor = self.cursor.next
        
        node = ListNode(value)
        previous.next = node
        self.cursor = node

        return None
    
    # TODO: add check for negative index
    def insert(self, index: int, value: int) -> None:
        if index == 0:
            self.push(value)
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
        self.cursor = node

        return None
    
    def delete(self, index: int) -> None:
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
numbers.append(0)
numbers.append(1)
numbers.append(2)
numbers.delete(-1)

numbers.listAll()