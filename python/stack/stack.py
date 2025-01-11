class Node:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None    # Pointer to the next node in the stack (initially None)

class Stack:
    def __init__(self, value):
        new_node = Node(value)  # Create a new node to initialize the stack
        self.top = new_node     # Set the top of the stack to the new node
        self.height = 1         # Track the height (number of elements) in the stack

    # Traverse the stack and print each node's value
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    # Add a new node with the given value to the top of the stack
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node  # If stack is empty, set top to new node
        else:
            new_node.next = self.top  # Set new node's next pointer to the current top
            self.top = new_node       # Set top to the new node
        self.height += 1  # Increment the height of the stack

    # Remove and return the top element of the stack
    def pop(self):
        if self.is_empty():
            return None  # Return None if the stack is empty
        temp = self.top  # Store the current top node
        self.top = self.top.next  # Set the new top to the next node
        self.height -= 1  # Decrement the height of the stack
        return temp  # Return the removed node

    # Return the value of the top element without removing it
    def peek(self):
        if self.is_empty():
            return None  # Return None if the stack is empty
        return self.top.value  # Return the value of the top node

     # Check if the stack is empty (i.e., top is None)
    def is_empty(self):
        return self.top is None
