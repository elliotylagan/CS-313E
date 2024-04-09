# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2: EPY82

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

    # Return True if both trees are similar. False otherwise.
    # tree is also a Tree type
    def is_similar(self, tree):
        realRoot = self.root
        fakeRoot = tree.root

        return is_similar_helper(realRoot, fakeRoot)
    # Return a list of nodes at a given level from left to right.
    def get_level(self, level):
        result = []
        current = self.root

        get_level_helper(current, 0, level, result)

        return result
    # Return the height of the tree
    def get_height(self):
        return get_height_helper(self.root, 0)
    # Return the number of nodes in the tree.
    def num_nodes(self):
        if self.root is None:
            return 0
        return num_nodes_helper(self.root, 1)
    # Returns the range of values stored in the tree.
    def range(self):
        if self.root is None:
            return 0
        min = self.root.data
        max = self.root.data
        return range_helper(self.root, min, max)

    # Returns the list of the node that you see from left side.
    # The order of the output should be from top to down.
    def left_side_view(self):
        result = []
        
        for i in range(self.get_height):
            result.append(self.get_level(i)[0])       

        return result

    # Returns the sum of the value of all leaves.
    def sum_leaf_nodes(self):
        if self.root is None:
            return 0
        return sum_leaf_nodes_helper(self.root)


def is_similar_helper(real, fake):
        if real.data != fake.data:
            return False
        if real.data is None and fake.data is None:
            return True
        return is_similar_helper(real.left, fake.left) and is_similar_helper(real.right, fake.right)

def get_level_helper(current, current_level, level, result):
        if current_level > level:
            return
        if current.data is None:
            return
        if current_level == level:
            result.append(current.data)
        
        get_level_helper(current.left, current_level + 1, level, result)
        get_level_helper(current.right, current_level+1, level, result)
        return

def get_height_helper(current, height):
    if current.data is None:
        return height
    else:
        height += 1
    return max(get_height_helper(current.left, height), get_height_helper(current.right, height))
    
def num_nodes_helper(current, numNodes):
    if current.data is None:
        return
    numNodes += 1
    
    num_nodes_helper(current.left, numNodes)
    num_nodes_helper(current.right, numNodes)
    return numNodes

def range_helper(current, min, max):
    if current.data is None:
        return
    if current.data > max:
        max = current.data
    if current.data < min:
        min = current.data

    range_helper(current.left, min, max)
    range_helper(current.right, min, max)

    return max - min

def sum_leaf_nodes_helper(current, sum): #fix this
    if current.data is None:
        return sum
    if is_leaf(current):
        return sum + current.data

    sum = sum_leaf_nodes_helper(current.left, sum)
    sum = sum_leaf_nodes_helper(current.right, sum)
    return sum

def is_leaf(current):
    if current.left.data is not None:
        return False
    if current.right.data is not None:
        return False
    return True

def main():
    """Main function. Feel free to write your own code here to test."""
    
if __name__ == "__main__":
    main()
