class Node:
    # Initializes a node with a given value
    def __init__(self, value):
        self.value = value  # Data value
        self.next = None    # Pointer to the next node

class LinkedList:
    # Initializes the linked list with a single node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node  # Points to the first node (head)
        self.tail = new_node  # Points to the last node (tail)
        self.length = 1       # Tracks the length of the list

    # Prints all values in the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)  # Print current node's value
            temp = temp.next   # Move to the next node

    # Adds a new node to the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
        else:
            # Add new node after the current tail and update tail pointer
            self.tail.next = new_node
        self.tail = new_node  # Update tail to the new node
        self.length += 1      # Increment the length of the list
        return True

    # Removes and returns the last node from the list
    def pop(self):
        if self.head is None:
            return None  # If list is empty, return None

        temp = self.head
        if self.length == 1:
            # If there's only one node, set head and tail to None
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        # Traverse to the second-to-last node
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev      # Update tail to the second-to-last node
        self.tail.next = None # Remove reference to the last node
        self.length -= 1      # Decrement the length of the list
        return temp

    # Adds a new node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current head and update head pointer
            new_node.next = self.head
            self.head = new_node
        self.length += 1      # Increment the length of the list
        return True

    # Removes and returns the first node from the list
    def remove_first(self):
        if self.head is None:
            return None  # If list is empty, return None
        temp = self.head
        self.head = self.head.next  # Update head to the next node
        temp.next = None  # Remove reference from the removed node
        self.length -= 1
        if self.length == 0:
            # If the list is now empty, set tail to None
            self.tail = None
        return temp

    # Returns the node at the given index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None  # Return None if index is out of bounds
        temp = self.head
        for _ in range(index):
            temp = temp.next  # Traverse to the node at the given index
        return temp

    # Updates the value of the node at the given index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value  # Update the value of the node
            return True
        return False  # Return False if index is out of bounds

    # Inserts a node at a specified index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False  # Return False if index is invalid
        if index == 0:
            return self.prepend(value)  # Use prepend if inserting at the head
        if index == self.length:
            return self.append(value)   # Use append if inserting at the tail

        # Insert at the middle of the list
        new_node = Node(value)
        temp = self.get(index-1)  # Get node at the previous index
        new_node.next = temp.next # Link new node to the next node
        temp.next = new_node       # Link previous node to the new node
        self.length += 1           # Increment the length of the list
        return True

    # Removes and returns the node at a specified index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None  # Return None if index is out of bounds
        if index == 0:
            return self.remove_first()  # Use remove_first if removing the head
        if index == self.length-1:
            return self.pop()           # Use pop if removing the tail

        # Remove a node in the middle of the list
        prev = self.get(index-1)   # Get the node before the one to be removed
        temp = prev.next           # Node to be removed
        prev.next = temp.next      # Bypass the node to be removed
        temp.next = None           # Remove reference to the next node
        self.length -= 1           # Decrement the length of the list
        return temp

    # Reverses the linked list in place
    def reverse(self):
        if self.head is None:
            return  # If the list is empty, do nothing

        previous = None
        current = self.head
        newTail = self.head  # The old head will become the new tail

        while current:
            nextNode = current.next  # Store the next node
            current.next = previous  # Reverse the link
            previous = current       # Move previous to the current node
            current = nextNode       # Move current to the next node

        self.head = previous  # Set the new head (which was the old tail)
        self.tail = newTail   # Set the new tail (which was the old head)
        self.tail.next = None # Ensure the new tail points to None
