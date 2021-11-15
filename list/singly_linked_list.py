class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.cursor = self.head
    
    # O(n)
    def get_node(self, value):
        cursor = self.head

        while cursor is not None:
            if cursor.value == value:
                return cursor
            cursor = cursor.next

        return None
    
    # O(n)
    def find_value(self, index: int):
        cursor = self.head
        count = 0

        while cursor is not None:
            if count == index:
                return cursor.value
            cursor = cursor.next
            count = count + 1
        
        raise IndexError("Index was out of range")

    # O(1)
    def push(self, value):
        new_node = ListNode(value, self.head)
        self.head = new_node
    
    # O(n)
    # TODO: make aditional pointer 'tail' to append items at constant time O(1)
    def append(self, value):
        if self.head is None:
            self.push(value)
            return None
        
        cursor = self.head

        while cursor is not None:
            previous = cursor
            cursor = cursor.next
        
        new_node = ListNode(value)
        previous.next = new_node
    
    # O(n)
    def insert(self, value, index: int):
        if index < 0:
            raise IndexError("Index was out of range")

        if index == 0:
            self.push(value)
            return None
        
        cursor = self.head

        for i in range(index - 1):
            if cursor is not None:
                cursor = cursor.next

        if cursor is None:
            raise IndexError("Index was out of range")

        previous = cursor
        following = cursor.next

        new_node = ListNode(value, following)
        previous.next = new_node
    
    # O(n)
    def delete(self, index: int):
        if index < 0:
            raise IndexError("Index was out of range")
        
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return None

        cursor = self.head

        for i in range(index - 1):
            if cursor is not None:
                cursor = cursor.next

        if cursor is None:
            raise IndexError("Index was out of range")
        
        following = cursor.next.next
        cursor.next = following
    
    # O(1)
    def remove(self):
        if self.head is not None:
            self.head = self.head.next
    
    # O(n)
    def count(self) -> int:
        cursor = self.head
        count = 0

        while cursor is not None:
            cursor = cursor.next
            count = count + 1
        
        return count
    
    def format(self) -> str:
        cursor = self.head
        result = ""

        while cursor is not None:
            result += str(cursor.value) + ", "
            cursor = cursor.next
        
        result = "[" + result[:-2] + "]"

        return result

    # TODO: create a method for reversing the list


numbers = SinglyLinkedList()
numbers.append(0)
numbers.append(1)
numbers.append(2)
numbers.push(7)

numbers.insert(9, 1)

numbers.remove()

print(numbers.format())