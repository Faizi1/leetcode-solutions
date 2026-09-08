'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# A linked list is just a few nodes connected together.
# 10 → 20 → 30 → None
# Each node has:
# data → the value
# next → where the next node is

# Example:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes
node1.next = node2
node2.next = node3


# Start from first node
current = node1

while current:
    print(current.data)
    current = current.next
# --------------------
