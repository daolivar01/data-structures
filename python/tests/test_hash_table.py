import pytest
from hash_table import HashTable

@pytest.fixture
def create_table():
    # Fixture to initialize a HashTable with some key-value pairs
    ht = HashTable()
    ht.set_item('apple', 10)
    ht.set_item('banana', 20)
    ht.set_item('orange', 30)
    return ht

def test_set_item(create_table):
    # Test that items are correctly added to the HashTable
    ht = create_table
    assert ht.get_item('apple') == 10
    assert ht.get_item('banana') == 20
    assert ht.get_item('orange') == 30

def test_get_item(create_table):
    # Test that values are correctly retrieved using their keys
    ht = create_table
    assert ht.get_item('apple') == 10
    assert ht.get_item('banana') == 20
    assert ht.get_item('orange') == 30
    assert ht.get_item('grape') is None  # Test for non-existent key

def test_collision_handling():
    # Test that the HashTable can handle key collisions by chaining
    ht = HashTable()
    ht.set_item('abc', 100)  # Suppose 'abc' and 'cba' cause a collision
    ht.set_item('cba', 200)  # Different key, same index
    assert ht.get_item('abc') == 100
    assert ht.get_item('cba') == 200

def test_keys(create_table):
    # Test that all keys are returned correctly from the HashTable
    ht = create_table
    keys = ht.keys()
    assert 'apple' in keys
    assert 'banana' in keys
    assert 'orange' in keys
    assert 'grape' not in keys  # Key doesn't exist

def test_empty_table():
    # Test the behavior of the HashTable when no items are present
    ht = HashTable()
    assert ht.get_item('apple') is None  # No key should be found
    assert ht.keys() == []  # No keys should exist
