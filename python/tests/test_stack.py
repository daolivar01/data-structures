import pytest
from stack import Stack

@pytest.fixture
def create_stack():
    stack = Stack(1)  # Initialize stack with a value of 1
    return stack

def test_push(create_stack):
    stack = create_stack
    stack.push(2)
    assert stack.top.value == 2  # The top value should be 2 after pushing
    assert stack.height == 2  # Stack height should increase to 2

    stack.push(3)
    assert stack.top.value == 3  # The top value should be 3 after another push
    assert stack.height == 3  # Stack height should increase to 3

def test_pop(create_stack):
    stack = create_stack
    popped_node = stack.pop()
    assert popped_node.value == 1  # Popped value should be the initial value (1)
    assert stack.height == 0  # Stack should be empty after the pop

    # Edge case: popping from an empty stack
    assert stack.pop() is None  # Should return None when popping from an empty stack
    assert stack.height == 0  # Stack height should remain 0

def test_peek(create_stack):
    stack = create_stack
    assert stack.peek() == 1  # The top value should be 1

    stack.push(2)
    assert stack.peek() == 2  # The top value should be 2 after pushing

    stack.pop()
    assert stack.peek() == 1  # The top value should revert to 1 after popping

def test_is_empty(create_stack):
    stack = create_stack
    assert stack.is_empty() is False  # Stack should not be empty

    stack.pop()  # Remove the only element
    assert stack.is_empty() is True  # Now the stack should be empty
