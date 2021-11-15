import unittest

from list.singly_linked_list import SinglyLinkedList

class TestGetNodeFunction(unittest.TestCase):

    # Test case: [2, 3, 0, 1]
    test_list = SinglyLinkedList()

    test_list.append(2)
    test_list.append(3)
    test_list.append(0)
    test_list.append(1)

    def test_get_1st_returns_3(self):
        self.assertEqual(self.test_list.get_node(1), 3)
    
    def test_get_0th_returns_2(self):
        self.assertEqual(self.test_list.get_node(0), 2)

    def test_get_3rd_returns_1(self):
        self.assertEqual(self.test_list.get_node(3), 1)
    
    def test_get_minus_5th_returns_minus_1(self):
        self.assertEqual(self.test_list.get_node(-5), -1)

    def test_get_99th_returns_minus_1(self):
        self.assertEqual(self.test_list.get_node(99), -1)

class TestAddAtHeadFunction(unittest.TestCase):

    # Test case: [2, 3, 0, 1]
    test_list = SinglyLinkedList()

    test_list.append(2)
    test_list.append(3)
    test_list.append(0)
    test_list.append(1)
    
    def test_addAtHead_7(self):
        self.test_list.push(7)
        self.assertEqual(self.test_list.head.value, 7)

class TestAddAtTailFunction(unittest.TestCase):

    # Test case: [2, 3, 0, 1]
    test_list = SinglyLinkedList()

    test_list.append(2)
    test_list.append(3)
    test_list.append(0)
    test_list.append(1)

    def test_addAtTail_8(self):
        self.test_list.append(8)
        self.assertEqual(self.test_list.cursor.value, 8)
    
    def test_addAtTail_when_list_is_empty(self):
        empty_list = SinglyLinkedList()
        empty_list.append(5)
        self.assertEqual(empty_list.cursor, empty_list.head)

class TestAddAtIndexFunction(unittest.TestCase):

    # Test case: [2, 3, 0, 1]
    test_list = SinglyLinkedList()

    test_list.append(2)
    test_list.append(3)
    test_list.append(0)
    test_list.append(1)

    def test_addAtIndex_0(self):
        list_ = self.test_list
        list_.insert(0, 7)
        self.assertEqual(list_.head.value, 7)

    def test_addAtIndex_4(self):
        list_ = self.test_list
        list_.insert(4, 8)
        self.assertEqual(list_.cursor.value, 8)
    
    def test_addAtIndex_2(self):
        list_ = self.test_list
        list_.insert(2, 9)
        self.assertEqual(list_.cursor.value, 9)
    
    def test_addAtIndex_minus_1(self):
        list_ = self.test_list
        list_.insert(-1, 9)
        self.assertEqual(list_.cursor.value, 2)

    def test_addAtIndex_5(self):
        list_ = self.test_list
        list_.insert(5, 10)
        self.assertEqual(list_.cursor, None)

class TestDeleteAtIndexFunction(unittest.TestCase):

    # Test case: [2, 3, 0, 1]
    test_list = SinglyLinkedList()

    test_list.append(2)
    test_list.append(3)
    test_list.append(0)
    test_list.append(1)

    def test_deleteAtIndex_0(self):
        list_ = self.test_list
        list_.delete(0)
        self.assertEqual(list_.head.value, 3)
    
    def test_deleteAtIndex_2(self):
        list_ = self.test_list
        list_.delete(2)
        self.assertEqual(list_.get_node(2), 1)
    
    def test_deleteAtIndex_4(self):
        list_ = self.test_list
        list_.delete(4)
        self.assertEqual(list_.head.value, 3)
