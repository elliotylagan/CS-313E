# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:EPY82

import sys
from collections import deque

class Stack:
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

    def __str__(self):
        """String representation of the stack"""
        return str(self.items)

class Queue:
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

    def __str__(self):
        """String representation of the queue"""
        return str(self.q)

class Vertex:
    """Vertex Class using properties and setters for better encapsulation."""

    def __init__(self, label):
        self.__label = label
        self.visited = False

    @property
    def visited(self):
        """Property to get the visited status of the vertex."""
        return self.__visited

    @visited.setter
    def visited(self, value):
        """Setter to set the visited status of the vertex."""
        if isinstance(value, bool):
            self.__visited = value
        else:
            raise ValueError("Visited status must be a boolean value.")

    @property
    def label(self):
        """Property to get the label of the vertex."""
        return self.__label

    def __str__(self):
        """String representation of the vertex"""
        return str(self.__label)


class Graph:
    """A Class to present Graph."""

    def __init__(self):
        self.vertices = []  # a list of vertex objects
        self.adjacency_matrix = []  # adjacency matrix of edges

    def has_vertex(self, label):
        """Check if a vertex is already in the graph"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return True
        return False

    def get_index(self, label):
        """Given a label get the index of a vertex"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return i
        return -1

    def add_vertex(self, label):
        """Add a Vertex with a given label to the graph"""
        '''adds to both list of Vertexes and expands matrix'''
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            self.adjacency_matrix[i].append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(num_vertices):
            new_row.append(0)
        self.adjacency_matrix.append(new_row)

    def add_edge(self, start, finish):
        """Add unweighted directed edge to graph"""
        '''start and finish are indexes'''
        self.adjacency_matrix[start][finish] = 1

    def get_adjacent_vertices(self, vertex_index):
        """Return adjacent vertex indices to vertex_index"""
        '''returns list of indexes'''
        vertices = []
        num_vertices = len(self.vertices)
        for j in range(num_vertices):
            if self.adjacency_matrix[vertex_index][j]:
                vertices.append(j)
        return vertices


    def has_cycle(self): # done
        '''
        Determine whether or not the graph has a cycle
        Return as a boolean value
        '''
        visited = [] #list of visited
        if self.has_cycle_helper(0, visited):
            return True
        return False
    
    def has_cycle_helper(self, current_index, visited): # done
        '''
        recursive call of has_cycle()
        '''
        new_adjacents = self.get_adjacent_vertices(current_index)
        if current_index in visited:
            return True
        visited.append(current_index)
        # print(current_index, new_adjacents, visited)
        if not new_adjacents:
            visited.pop(-1)
            return
        for adjacent in new_adjacents:
            if self.has_cycle_helper(adjacent, visited):
                return True
        return False

    def get_registration_plan(self): #need to complete
        '''
        Return a valid ordering of courses to take for registration as a list of vertex labels.
        This method assumes that there is a valid registration plan.
        '''

        # Because we don't want to destroy the original graph,
        # we have defined helper functions that work with a copy of the
        # adjacency matrix and vertices. This is also a hint that we
        # suggest you to manipulate the graph copy to solve this method.

        # We encourage you to use these variables and functions, although
        # if you come up with a solution that doesn't, you may delete them.

        # temp_vertices = list(self.vertices)
        # temp_matrix = []
        # for row in self.adjacency_matrix:
        #     temp_matrix.append(list(row))

        def is_starting_point(label): #added myself
            '''
            returns True if has no pre-requisites
            pre-requisites determined by column having all zeros
            '''
            index = self.get_index(label)
            for row in self.adjacency_matrix:
                if row[index] == 1:
                    return False
            return True
        
        def can_take(label, completed):
            '''
            returns bool of if you can take the class based on pre-reqs
            completed is a list
                indexes represent indexes 1:1
                values are 0 or 1, 0 is never taken 1 is already taken
            '''
            index = self.get_index(label)
            if completed[index] == 1:
                return False
            for row_num  in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[row_num][index] == 1:
                    if completed[row_num] == 0:
                        return False
            return True
        
        def get_path(label, result):
            '''
            finds all possible paths from starting point
            '''
            temp = []
            get_path_helper(label, temp, result)

            return result
        
        def get_path_helper(label, temp, result):
            '''
            helper for get_path
            '''
            return result

        # def get_index_from_copy(label, vertices_copy):
        #     """Given a label get the index of a vertex in the copy of the vertices list"""
        #     num_vertices = len(vertices_copy)
        #     for i in range(num_vertices):
        #         if label == vertices_copy[i].label:
        #             return i
        #     return -1

        # def delete_vertex_from_copy(vertex_label, adjacency_matrix_copy, vertices_copy):
        #     """delete vertex from the copy of the adjacency matrix and vertices list"""
        #     index = get_index_from_copy(vertex_label, vertices_copy)

        #     for row in adjacency_matrix_copy:
        #         row.pop(index)
        #     adjacency_matrix_copy.pop(index)
        #     vertices_copy.pop(index)

        courses = []
        courses_taken = [0 for _ in range(len(self.vertices))]

        ##### TODO: Add code here #####
        while len(courses) < len(self.vertices):
            for vertex in self.vertices:
                label = vertex.label
                index = self.get_index(label)
                if courses_taken[index] == 1:
                    continue
                if can_take(label, courses_taken):
                    courses.append(label)
                    courses_taken[index] = 1
            
                # print("for loop  ", courses, courses_taken)

            # print("while loop", courses, courses_taken)



        return courses

# Read the input file and construct the graph. The output code has been written for you.
def main(): #done
    '''
    create Graph object and runs course
    all # are debugging
    '''
    graph = Graph()

    num_verticies = sys.stdin.readline()
    for _ in range(int(num_verticies)):
        graph.add_vertex(sys.stdin.readline().strip())
    num_edges = sys.stdin.readline()
    # for i in range(len(graph.vertices)):
    #     print(graph.vertices[i].label)
    for _ in range(int(num_edges)):
        start, end = sys.stdin.readline().strip().split(" ")
        # print(start, end)
        start = graph.get_index(start)
        end = graph.get_index(end)
        # print(start, end)
        graph.add_edge(start, end)
        # print(start, end, graph.adjacency_matrix)

    # print(graph.adjacency_matrix)

    ####################################################################################
    # DO NOT CHANGE ANYTHING BELOW THIS
    if graph.has_cycle():
        print("Registration plan invalid because a cycle was detected.")
    else:
        print("Valid registration plan detected.")
        print()
        print("Registration plan: ")
        courses = graph.get_registration_plan()        
        print(courses)

main()
