# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2: epy82

'''
Implements polynomials as a singly linked list with coeff and exp attributes.
Uses a sentinel node without head or tail attributes. Main function accepts
input file of format:

number of terms in first polynomial (n)
1st term (int: coeff, int: exp)     e.g   3 7
2nd term
...
nth term
***blank line***
number of terms in second polynomial (m)
1st term
2nd term
...
mth term

Returns the addition and multiplication of polynomials in descending order

(coeff, exp) + (coeff, exp)

'''

import sys


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data attribute, this node class has both 
    a coefficient and an exponent attribute, which is used to represent each 
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    '''Class we modify in order to implement polynomial addition
    and multiplication'''

    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        self.dummy = Node(None, None)

        # self.head = None

    def insert_term(self, coeff, exp):
        '''
        Insert the term with the coefficient coeff and exponent exp 
        into the polynomial. If a term with that exponent already exists, 
        add the coefficients together. You must keep the terms in 
        descending order by exponent.
        '''

        # If first node is empty, insert as first node
        first = self.dummy.next

        if first is None:
            if coeff != 0:
                self.dummy.next = Node(coeff, exp)
            return

        # Else, keep track of previous and current nodes
        prev = self.dummy
        current = self.dummy.next

        # If current node is populated, compare exponents
        while current is not None:
            exp1 = current.exp

            # If exp is greater than current exponent, insert Node before
            if exp > exp1:
                prev.next = Node(coeff, exp)
                prev.next.next = current
                return

            # If exp equals current exponent, add coefficients
            if exp == exp1:
                current.coeff += coeff

                # If addition causes coefficient to disappear, remove node
                if current.coeff == 0:
                    prev.next = current.next
                    return
                return

            # Increment prev and current nodes by one position
            current = current.next
            prev = prev.next

        # If we run out of nodes, insert at end
        prev.next = Node(coeff, exp)
        return

    def add(self, p):
        '''
        Add a polynomial p to the polynomial and return the resulting 
        polynomial as a new linked list.
        '''
        result = LinkedList()       # New linked list result

        list1 = self                # First list is current
        list2 = p                   # Second list is p

        term = list1.dummy.next     # Check first term of current

        # While there is a term to add, insert it
        while term is not None:
            if term.coeff != 0:
                result.insert_term(term.coeff, term.exp)
            term = term.next

        term = list2.dummy.next     # Check first term of p

        # While there is a term to add, insert it
        while term is not None:
            if term.coeff != 0:
                result.insert_term(term.coeff, term.exp)
            term = term.next

        return result

    def mult(self, p):
        '''
        Multiply a polynomial p with the polynomial and return the 
        product as a new linked list.'

        '''
        result = LinkedList()       # New linked list result

        # If current polynomial is empty, just add p
        if self.dummy.next is None:
            return result.add(p)

        # If p is empty, just add current
        if p.dummy.next is None:
            return result.add(self)

        # Else, complete multiplication
        # Outer loop through each term of result
        # Inner loop multiplying by each term of p
        outer = self.dummy.next

        while outer is not None:
            inner = p.dummy.next
            exp1 = outer.exp
            coeff1 = outer.coeff
            while inner is not None:
                exp2 = inner.exp
                coeff2 = inner.coeff
                if coeff1 != 0 and coeff2 != 0:
                    result.insert_term(coeff1*coeff2, exp1+exp2)
                inner = inner.next
            outer = outer.next

        return result

    def __str__(self):
        '''
        Return a string representation of the polynomial.
        '''
        to_print = []

        term = self.dummy.next

        while term is not None:
            element = (term.coeff, term.exp)
            to_print.append(str(element))
            term = term.next

        to_print = " + ".join(to_print)

        return str(to_print)


def main():
    '''
    Executed the body of the program
    '''
    # read data from stdin and create polynomial p
    # read data from stdin and create polynomial q
    p = LinkedList()
    q = LinkedList()


    for _ in range(2):
        prange = input()
        print(prange)
        for _ in range(int(prange)):
            line = input()
            line = line.strip()
            data = line.split(" ")
            p.insert_term(int(data[0]), int(data[1]))
        
        input()
        
        qrange = input()
        for _ in range(int(qrange)):
            line = input()
            line = line.strip()
            data = line.split(" ")
            q.insert_term(int(data[0]), int(data[1]))


    # get sum of p and q as a new linked list and print sum
    print(p.add(q))

    # get product of p and q as a new linked list and print product
    print(p.mult(q))


if __name__ == "__main__":
    main()
