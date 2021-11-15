class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(n)
    def get_node(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next

        return None
    
    # O(n)
    def find_value(self, index: int):
        current = self.head
        count = 0

        while current is not None:
            if count == index:
                return current.value
            current = current.next
            count = count + 1
        
        raise IndexError("Index was out of range")

    # O(1)
    def push(self, value):
        new_node = ListNode(value, self.head)

        if self.head is None:
            self.tail = new_node

        self.head = new_node
    
    # O(1)
    def append(self, value):
        if self.head is None:
            self.push(value)
            return None
        
        new_node = ListNode(value)
        self.tail.next = new_node

        self.tail = new_node
    
    # O(n)
    def insert(self, value, index: int):
        if index < 0:
            raise IndexError("Index was out of range")

        if index == 0:
            self.push(value)
            return None
        
        current = self.head

        for i in range(index - 1):
            if current is not None:
                current = current.next

        if current is None:
            raise IndexError("Index was out of range")

        previous = current
        following = current.next

        new_node = ListNode(value, following)
        previous.next = new_node

        if following is None:
            self.tail = new_node
    
    # O(n)
    def delete(self, index: int):
        if index < 0:
            raise IndexError("Index was out of range")
        
        if index == 0 and self.head is not None:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return None

        current = self.head

        for i in range(index - 1):
            if current is not None:
                current = current.next

        if current is None:
            raise IndexError("Index was out of range")
        
        following = current.next.next
        current.next = following

        if following is None:
            self.tail = current
    
    # O(1)
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
        
        if self.head is None:
            self.tail = None
    
    # O(n)
    def count(self) -> int:
        current = self.head
        count = 0

        while current is not None:
            current = current.next
            count = count + 1
        
        return count
    
    def format(self) -> str:
        current = self.head
        result = ""

        while current is not None:
            result += str(current.value) + ", "
            current = current.next
        
        result = "[" + result[:-2] + "]"

        return result

    def reverse(self):
        previous = None
        current = self.head
        following = self.head

        self.tail = self.head
        
        while current is not None:
            following = following.next
            current.next = previous
            previous = current
            current = following
        
        self.head = previous
