"""
Basic Data Structures Implementation Templates
This module will contain implementations of fundamental data structures
covered in Module 1 of the course.
"""

# ===== Linear Data Structures =====

# Array/List
# Properties:
# - Fixed or dynamic size
# - Continuous memory allocation
# - O(1) access by index
# - O(n) for insertion/deletion in middle
# TODO: Implement Array Code
my_array = [1, 2, 3, 4, 5]

# Stack
# Properties:
# - LIFO (Last In First Out)
# - Push and Pop operations
# - Common uses: undo/redo, expression evaluation, backtracking
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
my_stack = Stack()

# Queue
# Properties:
# - FIFO (First In First Out)
# - Enqueue and Dequeue operations
# - Common uses: job scheduling, resource management
# TODO: Implement Queue Code

# Linked List
# Properties:
# - Dynamic size
# - Non-continuous memory allocation
# - O(1) insertion/deletion at known position
# - O(n) access by index
# TODO: Implement LinkedList Code

# ===== Non-Linear Data Structures =====

# Tree
# Properties:
# - Hierarchical structure
# - One root node
# - Each node can have multiple children
# - Common uses: file systems, organization charts
# TODO: Implement Tree Code

# Graph
# Properties:
# - Nodes/vertices connected by edges
# - Can be directed or undirected
# - Can be weighted or unweighted
# - Common uses: social networks, routing
# TODO: Implement Graph Code

# Hash Table
# Properties:
# - Key-value pairs
# - O(1) average case for insertion/deletion/lookup
# - Uses hash function for index calculation
# - Common uses: caching, symbol tables
# TODO: Implement HashTable Code

# Heap
# Properties:
# - Complete binary tree
# - Max-heap or Min-heap
# - O(log n) insertion/deletion
# - Common uses: priority queues, heap sort
# TODO: Implement Heap Code

"""
Note: Each data structure will be implemented in subsequent lessons.
This file serves as a roadmap for the implementations to come.
"""