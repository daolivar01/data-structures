import pytest
from queue_impl import Queue

# Pytest fixture to create a Queue
@pytest.fixture
def create_queue():
    queue = Queue(10)  # Initialize the queue with a value of 10
    return queue

# Test enqueue method
def test_enqueue(create_queue):
    queue = create_queue
    queue.enqueue(20)
    queue.enqueue(30)

    # Test first node value after enqueue
    assert queue.first.value == 10  # First node should still be 10
    # Test last node value after enqueue
    assert queue.last.value == 30  # Last node should now be 30
    # Test length after enqueue
    assert queue.length == 3  # Length should be 3

# Test dequeue method
def test_dequeue(create_queue):
    queue = create_queue
    queue.enqueue(20)
    queue.enqueue(30)

    dequeued_node = queue.dequeue()

    # Test value of dequeued node
    assert dequeued_node.value == 10  # First dequeued value should be 10
    # Test first node value after dequeue
    assert queue.first.value == 20  # First node should now be 20
    # Test length after dequeue
    assert queue.length == 2  # Length should be 2

    queue.dequeue()
    queue.dequeue()

    # Test if first and last are None after dequeuing all elements
    assert queue.first is None  # First should be None
    assert queue.last is None  # Last should be None
    # Test length after all dequeues
    assert queue.length == 0  # Length should be 0
    # Test if queue is empty
    assert queue.is_empty()  # Queue should be empty

# Test peek method
def test_peek(create_queue):
    queue = create_queue
    queue.enqueue(20)

    # Test peek value
    assert queue.peek() == 10  # Peek should return 10
    queue.dequeue()
    # Test peek value after dequeue
    assert queue.peek() == 20  # Peek should return 20 after dequeue

# Test is_empty method
def test_is_empty(create_queue):
    queue = create_queue

    # Test if queue is not empty initially
    assert not queue.is_empty()  # Queue should not be empty

    queue.dequeue()

    # Test if queue is empty after dequeueing the only element
    assert queue.is_empty()  # Queue should be empty

# Test dequeue method when queue is empty
def test_dequeue_empty(create_queue):
    queue = create_queue
    queue.dequeue()  # Dequeue the only element

    # Test dequeue when queue is empty
    assert queue.dequeue() is None  # Should return None when dequeuing from an empty queue
