import pytest
from doubly_linked_list import DoublyLinkedList

@pytest.fixture
def create_list():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    return dll

def test_append(create_list):
    dll = create_list
    assert dll.tail.value == 3
    assert dll.head.value == 1
    assert dll.length == 3

def test_pop(create_list):
    dll = create_list
    popped_node = dll.pop()
    assert popped_node.value == 3  # Popped value should be the last one (tail)
    assert dll.tail.value == 2  # Tail should be updated to 2
    assert dll.length == 2  # Length should decrease by 1

    # Edge case: popping from a list with 1 element
    dll.pop()
    dll.pop()
    assert dll.pop() is None  # Nothing to pop from empty list
    assert dll.length == 0  # Length should be 0

def test_prepend(create_list):
    dll = create_list
    dll.prepend(0)
    assert dll.head.value == 0  # New head should be the prepended value
    assert dll.length == 4  # Length should increase by 1

def test_pop_first(create_list):
    dll = create_list
    popped_node = dll.pop_first()
    assert popped_node.value == 1  # Popped value should be the first (head)
    assert dll.head.value == 2  # New head should be updated to 2
    assert dll.length == 2  # Length should decrease by 1

    # Edge case: popping first from list with 1 element
    dll.pop_first()
    dll.pop_first()
    assert dll.pop_first() is None  # Nothing to pop from empty list
    assert dll.length == 0  # Length should be 0

def test_get(create_list):
    dll = create_list
    assert dll.get(0).value == 1  # Get first element
    assert dll.get(1).value == 2  # Get second element
    assert dll.get(2).value == 3  # Get third element
    assert dll.get(3) is None  # Out of bounds index

def test_set_value(create_list):
    dll = create_list
    dll.set_value(1, 10)  # Set index 1 to 10
    assert dll.get(1).value == 10  # Value should be updated to 10
    assert dll.set_value(3, 20) is True  # Setting out of bounds should not fail silently

def test_insert(create_list):
    # Insert at the beginning
    assert create_list.insert(0, 5) is True  # Insert at the head of the list
    assert create_list.head.value == 5       # Head should now be the newly inserted node
    assert create_list.head.next.value == 1  # The next node should be the previous head's value (1)
    assert create_list.length == 4           # Length should increment by 1

    # Insert at the end
    assert create_list.insert(4, 15) is True  # Insert at the tail of the list
    assert create_list.tail.value == 15       # Tail should now be the newly inserted node
    assert create_list.tail.prev.value == 3  # The previous node of the tail should be the old tail
    assert create_list.length == 5            # Length should increment by 1

    # Insert in the middle
    assert create_list.insert(2, 12) is True  # Insert 12 between 5 and 1
    assert create_list.get(2).value == 12     # Node at index 2 should have value 12
    assert create_list.get(2).prev.value == 1  # Previous node should be 1
    assert create_list.get(2).next.value == 2  # Next node should be 2
    assert create_list.length == 6            # Length should increment by 1

    # Invalid index (negative index and out of bounds)
    assert create_list.insert(-1, 20) is False  # Negative index should return False
    assert create_list.insert(7, 25) is False   # Out of bounds index should return False
    assert create_list.length == 6             # Length should remain unchanged

def test_remove(create_list):
    dll = create_list

    # Test removing from the beginning
    removed_node = dll.remove(0)
    assert removed_node is not None  # Ensure a node was returned
    assert removed_node.value == 1  # The removed node should have value 1 (head)
    assert dll.length == 2  # Length should decrease by 1
    assert dll.head.value == 2  # The new head should be the second node
    assert dll.tail.value == 3  # The tail should remain the same (3)

    # Test removing from the end
    removed_node = dll.remove(dll.length - 1)
    assert removed_node is not None  # Ensure a node was returned
    assert removed_node.value == 3  # The removed node should have value 3 (tail)
    assert dll.length == 1  # Length should decrease by 1
    assert dll.tail.value == 2  # The tail should now be the remaining node (2)

    # Test removing from the middle (now there is only one node left)
    dll.append(4)  # Add a new element for this test
    dll.append(5)  # Add another element
    removed_node = dll.remove(1)  # Remove the node with value 4 (index 1)
    assert removed_node is not None  # Ensure a node was returned
    assert removed_node.value == 4  # The removed node should have value 4
    assert dll.length == 2  # Length should decrease by 1
    assert dll.get(0).value == 2  # The head should still be 2
    assert dll.get(1).value == 5  # The new tail should be 5

    # Test out-of-bounds indices
    assert dll.remove(-1) is None  # Negative index should return None
    assert dll.remove(3) is None   # Out of bounds index (greater than or equal to current length) should return None
    assert dll.length == 2  # Length should remain the same
