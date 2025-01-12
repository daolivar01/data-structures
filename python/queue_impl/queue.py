class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    # Initialize the queue with a single node
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node  # First (head) points to the new node
        self.last = new_node   # Last (tail) points to the new node
        self.length = 1        # Queue starts with length 1

    # Print all the elements in the queue
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    # Add a new node to the end (tail) of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            # If the queue is empty, both first and last point to the new node
            self.first = new_node
            self.last = new_node
        else:
            # Add the new node to the end of the queue and update the last pointer
            self.last.next = new_node
            self.last = new_node
        self.length += 1  # Increment the length of the queue

    # Remove and return the first node from the queue
    def dequeue(self):
        if self.is_empty():
            return None  # If the queue is empty, return None

        temp = self.first  # Store the current first node
        self.first = temp.next  # Move the first pointer to the next node
        temp.next = None  # Detach the dequeued node from the queue
        self.length -= 1  # Decrement the length of the queue

        if self.length == 0:
            # If the queue is now empty, reset the last pointer to None
            self.last = None

        return temp  # Return the dequeued node

    # Return the value of the first node without removing it
    def peek(self):
        if self.is_empty():
            return None  # If the queue is empty, return None
        return self.first.value  # Return the value of the first node

    # Check if the queue is empty
    def is_empty(self):
        return self.first is None
