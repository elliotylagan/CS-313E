import unittest

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        nodes_str = []
        current = self.head
        while current is not None:
            nodes_str.append(str(current))
            current = current.next
        nodes_str.append("None")
        output = " <-> ".join(nodes_str)
        return output

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self.tail = temp
            self.head = temp
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
        self.size += 1


    def insert(self, pos, item):
        '''
        inserts
        '''
        if pos > self.size:
            raise IndexError("Index out of bounds")

    def remove(self, item):
        pass

class TestDoublyLinkedList(unittest.TestCase):

    def test_0(self):
        my_list = DoublyLinkedList()
        my_list.add(44)
        self.assertEqual(my_list.size, 1, "Test 0 Failed - size is incorrect")
        self.assertEqual(str(my_list), "44 <-> None", "Test 0 Failed - list is incorrect")
        self._test_links(my_list, 0)

    def test_1(self):
        my_list = DoublyLinkedList()
        self.assertTrue(my_list.is_empty(), "Test 1 Failed")
        self._test_links(my_list, 1)

    def test_2(self):
        my_list = DoublyLinkedList()
        my_list.add(13)
        self.assertFalse(my_list.is_empty(), "Test 2 Failed")
        self._test_links(my_list, 2)

    def test_3(self):
        my_list = DoublyLinkedList()
        my_list.add(426)
        my_list.remove(426)
        self.assertTrue(my_list.is_empty(), "Test 3 Failed")
        self._test_links(my_list, 3)

    def test_4(self):
        my_list = DoublyLinkedList()
        with self.assertRaises(ValueError):
            my_list.remove(0)

    def test_5(self):
        my_list = DoublyLinkedList()
        my_list.add(42)
        my_list.add(231)
        my_list.remove(231)
        self.assertEqual(str(my_list.head), "42", "Test 5 Failed")
        self.assertEqual(my_list.size, 1, "Test 5 Failed - size is incorrect")
        self._test_links(my_list, 5)

    def test_6(self):
        my_list = DoublyLinkedList()
        my_list.add(42)
        my_list.add(231)
        my_list.add(111)
        my_list.remove(231)
        self.assertEqual(str(my_list), "111 <-> 42 <-> None", "Test 6 Failed")
        self._test_links(my_list, 6)

    def test_7(self):
        my_list = DoublyLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(3)
        self.assertEqual(str(my_list), "3 <-> 2 <-> 1 <-> None", "Test 7 Failed")
        self._test_links(my_list, 7)

    def test_8(self):
        my_list = DoublyLinkedList()
        my_list.append(72)
        self.assertEqual(str(my_list.head), "72", "Test 8 Failed")
        self._test_links(my_list, 8)

    def test_9(self):
        my_list = DoublyLinkedList()
        my_list.append(72)
        my_list.append(23)
        my_list.append(40)
        self.assertEqual(str(my_list), "72 <-> 23 <-> 40 <-> None", "Test 9 Failed")
        self._test_links(my_list, 9)

    def test_10(self):
        my_list = DoublyLinkedList()
        my_list.append(72)
        my_list.append(23)
        my_list.append(40)
        my_list.remove(23)
        self.assertEqual(my_list.size, 2, "Test 10 Failed - size is incorrect")
        self.assertEqual(str(my_list), "72 <-> 40 <-> None", "Test 10 Failed - list is incorrect")
        self._test_links(my_list, 10)

    def test_11(self):
        my_list = DoublyLinkedList()
        my_list.add(61)
        with self.assertRaises(IndexError):
            my_list.insert(2, 32)

    def test_12(self):
        my_list = DoublyLinkedList()
        my_list.add(61)
        my_list.add(12)

        my_list2 = DoublyLinkedList()
        my_list2.insert(0, 61)
        my_list2.insert(0, 12)

        self.assertEqual(str(my_list), str(my_list2), "Test 12 Failed")
        self._test_links(my_list, 12)
        self._test_links(my_list2, 12)

    def test_13(self):
        my_list = DoublyLinkedList()
        my_list.insert(0, 13)
        my_list.insert(1, 8)
        my_list.insert(2, 16)
        self.assertEqual(str(my_list), "13 <-> 8 <-> 16 <-> None", "Test 13 Failed")
        self._test_links(my_list, 13)

    # Additional method to test the links between nodes
    def _test_links(self, my_list, test_num):
        forward_contents = []
        current = my_list.head
        while current:
            forward_contents.append(str(current.data))
            current = current.next
        backward_contents = []
        current = my_list.tail
        while current:
            backward_contents.append(str(current.data))
            current = current.prev
        
        backward_contents = backward_contents[::-1]
        check = forward_contents == backward_contents
        forward_contents.append("None")
        backward_contents.insert(0, "None")
        assert check, "Test " + str(test_num) + " Failed - next/prev links don't match: " + \
                    " -> ".join(forward_contents) + " | " + " <- ".join(backward_contents)

if __name__ == '__main__':
    unittest.main()