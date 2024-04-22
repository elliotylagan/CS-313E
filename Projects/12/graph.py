
#  Name 1: Ryan Schlimme
#  EID 1: RJS4499

#  Name 2: Elliot Ylagan
#  EID 2: EPY82

'''Implements an image fill algorithm using graph structure'''


import os
import sys
from collections import deque

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------
os.system("")  # Enables printing colors on Windows
RESET_CHAR = "\u001b[0m"  # Code to reset the terminal color
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
BLOCK_CHAR = "\u2588"  # Character code for a block


def colored(text, color):
    """Wrap the string with the color code."""
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise ValueError(color + " is not a valid color!")
    return COLOR_DICT[color] + text


def print_block(color):
    """Print a block in the specified color."""
    print(colored(BLOCK_CHAR, color) * 2, end='')
# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


class Stack:  # predone
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self.items = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.items


class Queue:  # predone
    """Queue class for search algorithms."""

    def __init__(self):
        self.q = deque()

    def peek(self):
        """Get the front element of the queue."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.q[0]

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.q.append(item)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.q.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.q


class ColoredVertex:
    """Class for a graph vertex."""

    def __init__(self, index, x, y, color):  # predone
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    def add_edge(self, vertex_index):  # predone
        """Add an edge to another vertex."""
        self.edges.append(vertex_index)

    def is_visited(self):
        ''' returns bool of is_visited '''
        if self.visited is True:
            return True
        return False

    def get_color(self):
        ''' returns color '''
        return self.color

    def get_prev_color(self):
        ''' returns previous color '''
        return self.prev_color

    def visit_and_set_color(self, color):  # predone
        """Set the color of the vertex and mark it visited."""
        self.visited = True
        self.prev_color = self.color
        self.color = color
        print("Visited vertex " + str(self.index))

    def __str__(self):  # predone
        return f"index: {self.index}, color: {self.color}, x: {self.x}, y: {self.y}"


class ImageGraph: 
    """Class for the graph."""

    def __init__(self, image_size):  # predone
        self.vertices = []  # list of ColoredVertex objects
        self.image_size = int(image_size)

    def print_image(self):  # predone
        """Print the image formed by the vertices."""
        img = [["black" for _ in range(self.image_size)]
               for _ in range(self.image_size)]

        # Fill img array
        for vertex in self.vertices:
            img[vertex.y][vertex.x] = vertex.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # Print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):  # predone
        """Reset the visited flag for all vertices."""
        for vertex in self.vertices:
            vertex.visited = False

    def print_adjacency_matrix(self): 
        ''' prints adjacency matrix '''
        print("Adjacency matrix:")

        
        for row, _ in enumerate(self.vertices):
            for col, _ in enumerate(self.vertices):
                if col in self.vertices[row].edges:
                    print("1", end="")
                else:
                    print("0", end="")
            print()
        print()  

    def bfs(self, start_index, color):  
        '''
        Perform Breadth-First Search algorithm
        Don't remove the first 2 statements we provide
        you may choose to call print_images in this method for debugging yourself        
        '''
        self.reset_visited()
        print("Starting BFS; initial state:")
        # self.print_image #for debugging

        # prep for traversing
        visited = []  # list of visited indexes in bfs order
        bfs = Queue()  # Queue of indexes
        first_vertex = self.vertices[int(start_index)]
        first_vertex.visit_and_set_color(color)

        visited.append(first_vertex.index)
        bfs.enqueue(first_vertex.index)
        # uses Queue to finish the search
        while not bfs.is_empty():
            index = bfs.dequeue()
            current_vertex = self.vertices[index]
            for next_index in current_vertex.edges:
                next_vertex = self.vertices[next_index]
                # created the is_visited() method to avoid error ( 'bool' object is not callable )
                if not next_vertex.is_visited() and (next_vertex.get_color()
                                                     == first_vertex.get_prev_color()):
                    next_vertex.visit_and_set_color(color)
                    bfs.enqueue(next_index)
                    visited.append(next_vertex)
        # self.print_image()
        # print(visited)

    def dfs(self, start_index, color): 
        '''
        Perform Depth-First Search algorithm.
        Don't remove the first 2 statements we provide.
        you may choose to call print_images in this func method debugging yourself        
        '''
        self.reset_visited()
        print("Starting DFS; initial state:")
        # self.print_image()

        # prep for traversing
        visited = []  # list of visited indexes in dfs order
        dfs = Stack()  # Stack of indexes
        first_vertex = self.vertices[int(start_index)]
        dfs.push(first_vertex.index)

        # uses stack to finish the search
        while not dfs.is_empty():
            index = dfs.pop()
            current_vertex = self.vertices[index]
            if not current_vertex.is_visited() and (current_vertex.get_color()
                                                    == first_vertex.get_prev_color()):
                current_vertex.visit_and_set_color(color)
                visited.append(index)
                for i in range(len(current_vertex.edges)-1, -1, -1):
                    dfs.push(current_vertex.edges[i])


def create_graph(data):  
    '''create a graph from the input data'''

    # split the data by new line
    data = data.split("\n")
    line_num = 0
    # get size of image and number of vertices
    # create the ImageGraph
    size = data[line_num]
    line_num += 1
    blank_image = ImageGraph(size)

    # create vertices - vertex info has the format "x,y,color"
    for i in range(int(data[line_num])):
        x, y, z = data[i + line_num + 1].split(",")
        new_vertex = ColoredVertex(i, int(x), int(y), z)
        blank_image.vertices.append(new_vertex)
    line_num += int(data[line_num]) + 1

    # create edges between vertices - edge info has the format
    #   "from_index,to_index"
    # connect vertex A to vertex B and the other way around
    for i in range(int(data[line_num])):
        a, b = data[i + 1 + line_num].split(",")
        a, b = int(a), int(b)
        blank_image.vertices[a].edges.append(b)
        blank_image.vertices[b].edges.append(a)
    line_num += int(data[line_num]) + 1

    # read search starting position and color
    index, color = data[line_num].split(",")

    # return the ImageGraph, starting position, and color as a tuple in this order.
    return (blank_image, int(index), color)


def main(): 
    '''
    read input
    create graph, passing in data
    call print adjacency matrix
    run bfs
    reset by creating graph again
    run dfs    
    '''
    data = sys.stdin.read()
    graph, index, color = create_graph(data)
    graph.print_adjacency_matrix()
    graph.bfs(index, color)
    graph, index, color = create_graph(data)
    graph.dfs(index, color)
    graph.print_image()


if __name__ == "__main__":
    main()