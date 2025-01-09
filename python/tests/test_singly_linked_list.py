import pytest
from linked_list import LinkedList

@pytest.fixture
def create_list():
    # Create a new linked list with one node containing value 1
    return LinkedList(1)

def test_append(create_list):
    # Test appending to the linked list
    ll = create_list
    ll.append(2)
    ll.append(3)
    
    assert ll.head.value == 1  # Test head remains correct
    assert ll.tail.value == 3  # Test tail is updated correctly
    assert ll.length == 3      # Test list length is updated correctly

def test_pop(create_list):
    # Test popping the last node from the linked list
    ll = create_list
    ll.append(2)
    popped_node = ll.pop()
    
    assert popped_node.value == 2  # Test correct node is popped
    assert ll.tail.value == 1       # Test tail is updated after pop
    assert ll.length == 1           # Test list length is decremented

    # Test popping the last remaining node
    popped_node = ll.pop()
    assert popped_node.value == 1   # Test the last node is popped
    assert ll.head is None          # Test head is updated to None
    assert ll.tail is None          # Test tail is updated to None
    assert ll.length == 0           # Test list length is 0

def test_prepend(create_list):
    # Test prepending to the linked list
    ll = create_list
    ll.prepend(0)
    
    assert ll.head.value == 0  # Test head is updated correctly
    assert ll.tail.value == 1  # Test tail remains unchanged
    assert ll.length == 2      # Test list length is updated correctly

def test_remove_first(create_list):
    # Test removing the first node from the linked list
    ll = create_list
    ll.append(2)
    
    removed_node = ll.remove_first()
    assert removed_node.value == 1   # Test correct node is removed
    assert ll.head.value == 2        # Test head is updated to the next node
    assert ll.length == 1            # Test list length is decremented

    # Test removing the last remaining node
    removed_node = ll.remove_first()
    assert removed_node.value == 2   # Test the last node is removed
    assert ll.head is None           # Test head is updated to None
    assert ll.tail is None           # Test tail is updated to None
    assert ll.length == 0            # Test list length is 0

def test_get(create_list):
    # Test getting a node by index
    ll = create_list
    ll.append(2)
    ll.append(3)
    
    node = ll.get(1)
    assert node.value == 2  # Test correct node is retrieved by index

    node = ll.get(2)
    assert node.value == 3  # Test correct node is retrieved by index

    node = ll.get(3)
    assert node is None     # Test out-of-bounds index returns None

def test_set_value(create_list):
    # Test setting a node's value by index
    ll = create_list
    ll.append(2)
    
    assert ll.set_value(1, 20) == True  # Test setting a value at index 1
    assert ll.get(1).value == 20        # Test the value is updated

    assert ll.set_value(2, 30) == False  # Test out-of-bounds index returns False

def test_insert(create_list):
    # Test inserting a node at a specific index
    ll = create_list
    ll.append(2)
    
    ll.insert(1, 1.5)
    assert ll.get(1).value == 1.5  # Test node is inserted at index 1
    assert ll.length == 3          # Test list length is updated correctly

    ll.insert(0, 0)
    assert ll.head.value == 0      # Test node is inserted at the head
    assert ll.length == 4          # Test list length is updated correctly

    ll.insert(4, 3)
    assert ll.tail.value == 3      # Test node is inserted at the tail
    assert ll.length == 5          # Test list length is updated correctly

    assert ll.insert(6, 4) == False  # Test out-of-bounds insertion returns False

def test_remove(create_list):
    # Test removing a node by index
    ll = create_list
    ll.append(2)
    ll.append(3)
    
    removed_node = ll.remove(1)
    assert removed_node.value == 2  # Test correct node is removed
    assert ll.length == 2           # Test list length is decremented

    ll.remove(0)
    assert ll.head.value == 3       # Test head is updated correctly
    assert ll.length == 1           # Test list length is decremented

def test_reverse(create_list):
    # Test reversing the linked list
    ll = create_list
    ll.append(2)
    ll.append(3)
    ll.reverse()
    
    assert ll.head.value == 3  # Test head is updated after reverse
    assert ll.tail.value == 1  # Test tail is updated after reverse
    assert ll.get(1).value == 2  # Test node order is reversed
