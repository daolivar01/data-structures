class Node:
    def __init__(self, value):
        self.value = value  # Store the node's value
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node (for doubly linked list)

class DoublyLinkedList:
    # Initialize the list with one node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node  # Head points to the first node
        self.tail = new_node  # Tail points to the last node (same as head initially)
        self.length = 1  # Start with a list of length 1

     # Print the values of the list from head to tail
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

     # Add a node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            # If list is empty, set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, adjust the pointers to include the new node at the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  # Update tail to the new node
        self.length += 1  # Increase the list length
        return True

    # Remove the last node from the list
    def pop(self):
        if self.head is None:
            return None  # If list is empty, nothing to pop

        temp = self.tail
        if self.length == 1:
            # If there's only one node, reset head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, adjust the tail to point to the previous node
            self.tail = self.tail.prev
            self.tail.next = None  # Set new tail's next to None
            temp.prev = None  # Remove link to the previous node
        self.length -= 1  # Decrease list length
        return temp  # Return the popped node

     # Add a node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            # If list is empty, set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, adjust the pointers to include the new node at the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update head to the new node
        self.length += 1  # Increase the list length
        return True

    # Remove the first node from the list
    def pop_first(self):
        if self.head is None:
            return None  # If list is empty, nothing to pop

        temp = self.head
        if self.length == 1:
            # If there's only one node, reset head and tail to None
            self.head = None
            self.tail = None
        else:
            # Otherwise, adjust the head to point to the next node
            self.head = self.head.next
            self.head.prev = None  # Remove link to the popped node
            temp.next = None  # Remove link to the next node
        self.length -= 1  # Decrease list length
        return temp  # Return the popped node

    # Get the node at a specific index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None  # Return None if index is out of bounds
        temp = self.head
        if index < self.length / 2:
            # If index is in the first half, traverse from head
            for _ in range(index):
                temp = temp.next
        else:
            # If index is in the second half, traverse from tail
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp  # Return the node at the given index

    # Update the value of the node at a specific index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value  # Update node's value if found
        return True  # Always return True

    # Insert a new node at a specific index in the list
    def insert(self, index, value):
        # Return False if index is out of bounds (less than 0 or greater than the list's length)
        if index < 0 or index > self.length:
            return False  # Invalid index

        # If inserting at the beginning of the list, use the prepend method
        if index == 0:
            return self.prepend(value)

        # If inserting at the end of the list, use the append method
        if index == self.length:
            return self.append(value)

        # Create a new node with the given value
        new_node = Node(value)

        # Get the node just before the specified index
        before = self.get(index-1)
        # Get the node just after the specified index
        after = before.next

        # Update the new node's previous and next pointers
        new_node.prev = before
        new_node.next = after

        # Update the surrounding nodes to point to the new node
        before.next = new_node
        after.prev = new_node

        # Increment the length of the list
        self.length += 1

        # Return True to indicate successful insertion
        return True

    # Remove a node at a specific index in the list
    def remove(self, index):
        # Return False if index is out of bounds (less than 0 or greater than or equal to the list's length)
        if index < 0 or index >= self.length:
            return None  # Invalid index
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        # Get the node at the given index
        temp = self.get(index)

        # Adjust the pointers of the neighboring nodes to remove the node at index
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.prev = None
        temp.next = None

        self.length -= 1  # Decrease list length
        return temp # Return the removed node


