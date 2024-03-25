import unittest

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
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
        output = " -> ".join(nodes_str)
        return output

    def add(self, item):
        temp = Node(item, self.head)
        if self.head is None: 
            self.tail = temp
        self.head = temp
        self.size += 1

    def is_empty(self):
        return self.head is None

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(str(item) + " is not in list.")
        if previous is None:
            self.head = current.next
            if self.head is None:
                self.tail = None
        else:
            previous.next = current.next
            if current.next is self.tail:
                self.tail = previous
        self.size -= 1

    def search(self, item):
        pass
    
    def append(self, item):
        temp = Node(item)
        if self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    def insert(self, pos, item):
        if pos > self.size:
            raise IndexError("Index out of bounds")
        if pos == 0:
            self.add(item)
            return
        if pos == self.size:
            self.append(item)
            return
        
        temp = Node(item)
        current = self.head
        for _ in range(pos - 1):
            current = current.next
        temp.next = current.next
        current.next = temp
        self.size += 1
        
    
    def pop(self, pos=None):
        if self.size == 0:
            raise IndexError("List is empty")
        if pos is None:
            pos = self.size - 1
        elif pos >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        if pos == 0:
            self.head = current.next
        else:
            for _ in range(pos - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

class TestSinglyLinkedList(unittest.TestCase):

    def test_0(self):
        my_list = SinglyLinkedList()
        my_list.add(44)
        self.assertEqual(my_list.size, 1, "Test 0 Failed - size is incorrect")
        self.assertEqual(str(my_list), "44 -> None", "Test 0 Failed - list is incorrect")

    def test_1(self):
        my_list = SinglyLinkedList()
        self.assertTrue(my_list.is_empty(), "Test 1 Failed")

    def test_2(self):
        my_list = SinglyLinkedList()
        my_list.add(13)
        self.assertFalse(my_list.is_empty(), "Test 2 Failed")

    def test_3(self):
        my_list = SinglyLinkedList()
        my_list.add(426)
        my_list.remove(426)
        self.assertTrue(my_list.is_empty(), "Test 3 Failed")

    def test_4(self):
        my_list = SinglyLinkedList()
        with self.assertRaises(ValueError):
            my_list.remove(0)

    def test_5(self):
        my_list = SinglyLinkedList()
        my_list.add(42)
        my_list.add(231)
        my_list.remove(231)
        self.assertEqual(str(my_list.head), "42", "Test 5 Failed")
        self.assertEqual(my_list.size, 1, "Test 5 Failed - size is incorrect")

    def test_6(self):
        my_list = SinglyLinkedList()
        my_list.add(42)
        my_list.add(231)
        my_list.add(111)
        my_list.remove(231)
        self.assertEqual(str(my_list), "111 -> 42 -> None", "Test 6 Failed")

    def test_7(self):
        my_list = SinglyLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(3)
        self.assertTrue(my_list.search(1), "Test 7 Failed")

    def test_8(self):
        my_list = SinglyLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(3)
        self.assertTrue(my_list.search(3), "Test 8 Failed")

    def test_9(self):
        my_list = SinglyLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(3)
        self.assertFalse(my_list.search(0), "Test 9 Failed")

    def test_10(self):
        my_list = SinglyLinkedList()
        my_list.append(72)
        self.assertEqual(str(my_list.head), "72", "Test 10 Failed")

    def test_11(self):
        my_list = SinglyLinkedList()
        my_list.append(72)
        my_list.append(23)
        my_list.append(40)
        self.assertEqual(str(my_list), "72 -> 23 -> 40 -> None", "Test 11 Failed")

    def test_12(self):
        my_list = SinglyLinkedList()
        my_list.append(72)
        my_list.append(23)
        my_list.append(40)
        my_list.remove(23)
        self.assertEqual(my_list.size, 2, "Test 12 Failed - size is incorrect")
        self.assertEqual(str(my_list), "72 -> 40 -> None", "Test 12 Failed - list is incorrect")

    def test_13(self):
        my_list = SinglyLinkedList()
        my_list.add(61)
        with self.assertRaises(IndexError):
            my_list.insert(2, 32)

    def test_14(self):
        my_list = SinglyLinkedList()
        my_list.add(61)
        my_list.add(12)

        my_list2 = SinglyLinkedList()
        my_list2.insert(0, 61)
        my_list2.insert(0, 12)

        self.assertEqual(str(my_list), str(my_list2), "Test 14 Failed")

    def test_15(self):
        my_list = SinglyLinkedList()
        my_list.insert(0, 13)
        my_list.insert(1, 8)
        my_list.insert(2, 16)
        self.assertEqual(str(my_list), "13 -> 8 -> 16 -> None", "Test 15 Failed")

    def test_16(self):
        my_list = SinglyLinkedList()
        my_list.add(11)
        my_list.add(27)
        my_list.add(34)
        self.assertEqual(my_list.pop(1), 27, "Test 16 Failed")
        self.assertEqual(str(my_list), "34 -> 11 -> None", "Test 16 Failed - list is incorrect")

    def test_17(self):
        my_list = SinglyLinkedList()
        with self.assertRaises(IndexError):
            my_list.pop(2)

    def test_18(self):
        my_list = SinglyLinkedList()
        my_list.add(11)
        with self.assertRaises(IndexError):
            my_list.pop(2)
    
    def test_19(self):
        my_list = SinglyLinkedList()
        my_list.add(11)
        my_list.add(135)
        self.assertEqual(my_list.pop(), 11, "Test 19 Failed")
        self.assertEqual(my_list.size, 1, "Test 19 Failed")

if __name__ == '__main__':
    unittest.main()