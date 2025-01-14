import pytest
from binary_search_tree import BinarySearchTree  # Adjust this import according to the file structure

@pytest.fixture
def create_bst():
    bst = BinarySearchTree()  # Create an empty Binary Search Tree
    bst.insert(10)  # Insert initial value to set up the BST for tests
    return bst

def test_insert(create_bst):
    bst = create_bst
    # Test inserting new values
    assert bst.insert(5) is True  # Insert value 5 should return True
    assert bst.root.left.value == 5  # Check that 5 is inserted on the left of root

    assert bst.insert(15) is True  # Insert value 15 should return True
    assert bst.root.right.value == 15  # Check that 15 is inserted on the right of root

    # Test inserting duplicate values
    assert bst.insert(10) is False  # Inserting duplicate value 10 should return False

def test_contains(create_bst):
    bst = create_bst
    # Test for values that exist
    assert bst.contains(10) is True  # Should return True as 10 is in the BST
    assert bst.contains(5) is False  # Initially, 5 is not in the BST
    assert bst.contains(15) is False  # Initially, 15 is not in the BST

    # Insert values and check if they exist
    bst.insert(5)
    bst.insert(15)
    assert bst.contains(5) is True  # Now 5 should be found in the BST
    assert bst.contains(15) is True  # Now 15 should be found in the BST

    # Test for a value that doesn't exist
    assert bst.contains(20) is False  # 20 was not inserted, so it should return False
