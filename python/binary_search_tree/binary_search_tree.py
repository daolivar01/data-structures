class Node:
    def __init__(self, value):
        self.value = value     # The value stored in the node
        self.left = None       # Pointer to the left child of the node
        self.right = None      # Pointer to the right child of the node

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree as None

    def insert(self, value):
        # Insert a new node with the given value into the binary search tree
        new_node = Node(value)  # Create a new node with the value
        if self.root is None:  # If the tree is empty, set the root to the new node
            self.root = new_node
            return True

        # Traverse the tree to find the correct position for the new node
        temp = self.root
        while (True):
            if new_node.value == temp.value:  # If the value already exists, return False
                return False
            if new_node.value < temp.value:  # If the new value is smaller, go left
                if temp.left is None:  # If the left child is None, insert the new node here
                    temp.left = new_node
                    return True
                temp = temp.left  # Otherwise, continue traversing left
            else:  # If the new value is larger, go right
                if temp.right is None:  # If the right child is None, insert the new node here
                    temp.right = new_node
                    return True
                temp = temp.right  # Otherwise, continue traversing right

    def contains(self, value):
        # Check if a node with the given value exists in the binary search tree
        temp = self.root  # Start at the root
        while temp:
            if value < temp.value:  # If the value is smaller, move left
                temp = temp.left
            elif value > temp.value:  # If the value is larger, move right
                temp = temp.right
            else:  # If the value is found, return True
                return True
        return False  # Return False if the value is not found
