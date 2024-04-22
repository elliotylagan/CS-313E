# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2: EPY82

'''Implements binary tree node and tree classes'''

import sys
from collections import deque


class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create a new stack"""
        self.__s = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.__s[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.__s.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.__s.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.__s


class Queue:
    """Queue implementation as a deque"""

    def __init__(self):
        """Create a new queue"""
        self.__q = deque()

    def peek(self):
        """Get the value of the front item in the queue"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.__q[0]

    def enqueue(self, item):
        """Add an item to the queue"""
        self.__q.append(item)

    def dequeue(self):
        """Remove an item from the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.__q.popleft()

    def is_empty(self):
        """Check if the queue is empty"""
        return not self.__q


class Node:
    """Node class for representing a node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node."""
        if value is None or isinstance(value, int):
            self.__data = value
        else:
            raise ValueError("data must be an int or None.")

    @property
    def left(self):
        """Get the left child of the node."""
        return self.__left

    @left.setter
    def left(self, node):
        """Set the left child of the node."""
        if node is None or isinstance(node, Node):
            self.__left = node
        else:
            raise ValueError("left must be a Node or None.")

    @property
    def right(self):
        """Get the right child of the node."""
        return self.__right

    @right.setter
    def right(self, node):
        """Set the right child of the node."""
        if node is None or isinstance(node, Node):
            self.__right = node
        else:
            raise ValueError("right must be a Node or None.")


class Tree:
    """Tree class for representing a binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data into the binary search tree."""

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = self.root

            while current is not None:
                parent = current

                if data < current.data:
                    current = current.left
                else:
                    current = current.right

            if data < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def is_similar(self, tree):
        '''Return True if both trees are similar. False otherwise.
        tree is also a Tree type'''
        real_root = self.root
        fake_root = tree.root
        if real_root is None and fake_root is None:
            return True
        if real_root is None or fake_root is None:
            return False
        return is_similar_helper(real_root, fake_root)

    def get_level(self, level): #needs work (test cases 1 & 3)
        '''Return a list of nodes at a given level from left to right.'''
        result = []
        current = self.root
        get_level_helper(current, 0, level, result)
        return result

    def get_height(self):
        '''Return the height of the tree'''
        return get_height_helper(self.root, -1)

    def num_nodes(self):
        '''Return the number of nodes in the tree.'''
        if self.root is None:
            return 0
        return num_nodes_helper(self.root, 1)

    def range(self): #needs work (all test cases)
        '''Returns the range of values stored in the tree.'''
        if self.root is None:
            return 0
        max1 = get_max(self.root, self.root.data)
        min1 = get_min(self.root, self.root.data)

        print("max", max1, "min", min1)
        return max1 - min1

    def left_side_view(self):
        '''Returns the list of the node that you see from left side.
        The order of the output should be from top to down.'''
        result = []

        for i in range(self.get_height() + 1):
            result.append(self.get_level(i)[0])

        return result

    def sum_leaf_nodes(self):
        '''Returns the sum of the value of all leaves.'''
        if self.root is None:
            return 0

        sum1 = 0
        return sum_leaf_nodes_helper(self.root, sum1)


def is_similar_helper(real, fake):
    '''helper for is_similar()'''
    if real is None and real is None:
        return True
    if real is None or real is None:
        return False
    if real.data != fake.data:
        return False
    return is_similar_helper(real.left, fake.left) and is_similar_helper(real.right, fake.right)


def get_level_helper(current, current_level, level, result): #needs work (something about Node not having right or left children)
    '''helper for get_level()'''
    if current_level > level:
        return
    if current is None:
        return
    if current_level == level:
        result.append(current.data)

    get_level_helper(current.left, current_level + 1, level, result)
    get_level_helper(current.right, current_level + 1, level, result)
    return


def get_height_helper(current, height):
    '''helper for get_height()'''
    if current is None:
        return height
    height += 1
    return max(get_height_helper(current.left, height), get_height_helper(current.right, height))


def num_nodes_helper(current, num_nodes):
    '''helper for num_nodes()'''
    if current is None:
        return 0
    return num_nodes_helper(current.left, num_nodes) + 1 + num_nodes_helper(current.right, num_nodes)


def get_min(current, min):
    '''helper for range()'''
    if current is None:
        return min
    return get_min(current.left, min)

def get_max(current, max):
    '''helper for range()'''
    if current is None:
        return max
    return get_min(current.right, max)

def sum_leaf_nodes_helper(current, sum1):  # fix this
    '''helper for sum_leaf_nodes()'''
    if current is None:
        return sum1
    if is_leaf(current):
        return sum1 + current.data

    sum1 = sum_leaf_nodes_helper(current.left, sum1)
    sum1 = sum_leaf_nodes_helper(current.right, sum1)

    return sum1


def is_leaf(current):
    '''tests if node is a leaf'''
    if current.left is not None:
        return False
    if current.right is not None:
        return False
    return True


def main():
    """Just some garbage so import sys doesn't give a formatting error"""

    input()
    input()
    input()
    input1 = input()
    input1 = input1.strip()
    input1 = input1.split(" ")

    Tree1 = Tree()
    for num in input1:
        Tree1.insert(int(num))

    print(Tree1.get_level(2))
    print(Tree1.get_height())
    print(Tree1.num_nodes())
    print(Tree1.range())
    print(Tree1.left_side_view())
    print(Tree1.sum_leaf_nodes())


if __name__ == "__main__":
    main()