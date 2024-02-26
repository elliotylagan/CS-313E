"""
"""
# Name: Elliot Ylagan
# EID: EPY82

def row_major_traversal(grid):
    """
    reads a 2x2 array left to right, top to bottom

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            coord_list.append((row, col))
    return coord_list


def column_major_traversal(grid):
    """
    reads a 2x2 array top to bottom, right to left

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            coord_list.append((row, col))
    return coord_list

def row_zigzag_traversal(grid):
    """
    reads a 2x2 array alternating between right/left and left/right, going from top to bottom

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []
    for row in range(len(grid)):
        if is_even(row):
            for col in range(len(grid[row])):
                coord_list.append((row, col))
        else:
            for col in range(len(grid[row])-1, -1, -1):
                coord_list.append((row, col))
    return coord_list

def column_zigzag_traversal(grid):
    """
    reads a 2x2 array alternating between top/bottom and bottom/top, going from left to right

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []
    for col in range(len(grid[0])):
        if is_even(col):
            for row in range(len(grid)):
                coord_list.append((row, col))
        else:
            for row in range(len(grid) - 1, -1, -1):
                coord_list.append((row, col))
    return coord_list

def main_diagonal_traversal(grid):
    """
    reads a 2x2 array top right to bottom left in the direction of the main diagonal

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []

    for coord_diff in range(len(grid[0])-1, 0, -1):
        x = 0
        y = coord_diff - x
        while coord_diff == y - x and y < len(grid[0]) and x < len(grid):
            coord_list.append((x, y))
            x += 1
            y += 1

    for coord_diff in range(0, 1 - len(grid) -1, -1):
        y = 0
        x = y - coord_diff
        while coord_diff == y - x and y < len(grid[0]) and x < len(grid):
            coord_list.append((x, y))
            x += 1
            y += 1

    return coord_list


def secondary_diagonal_traversal(grid):
    """
    reads a 2x2 array top left to bottom right in the direction of the secondary diagonal

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    coord_list = []

    for coordSum in range(len(grid) + len(grid[0]) - 1):
        if coordSum < len(grid[0]):
            y = coordSum
        else:
            y = len(grid[0]) -1
        x = coordSum - y

        while coordSum == x + y and x < len(grid) and y >= 0:
            coord_list.append((x,y))
            x += 1
            y -= 1
    return coord_list

def spiral_traversal(grid):
    """
    reads a 2x2 array in a clockwise spiral order

    param: grid - a 2x2 array
    return: coord_list - a list of tuples of the corrdinates in the correct order
    """
    x = y = top = left = 0
    bottom = len(grid) - 1
    right = len(grid[0]) - 1
    coord_list = []

    while len(coord_list) < len(grid)*len(grid[0]):
        for i in range(left, right + 1):
            coord_list.append((x, y))
            if y == right:
                x += 1
            else:
                y += 1
        top += 1

        if len(coord_list) < len(grid)*len(grid[0]):
            for i in range(top, bottom + 1):
                coord_list.append((x, y))
                if x == bottom:
                    y -= 1
                else:
                    x += 1  
            right -= 1

        if len(coord_list) < len(grid)*len(grid[0]):
            for i in range(right, left - 1, -1):
                coord_list.append((x, y))
                if y == left:
                    x -= 1
                else:
                    y -= 1
            bottom -= 1

        if len(coord_list) < len(grid)*len(grid[0]):
            for i in range(bottom, top - 1, -1):
                coord_list.append((x, y))
                if x == top:
                    y += 1
                else:
                    x -= 1
            left += 1
    return coord_list


def is_even(num):
    """
    determines if a number is even

    param: num - the integer in question
    return: bool - whether or not the integer is even
    """
    if num % 2 == 0:
        return True
    return False

