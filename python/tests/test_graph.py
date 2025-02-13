import pytest
from graph import Graph

# Fixture to create a graph with three vertices and edges for testing.
@pytest.fixture
def create_graph():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    return g

# Tests the add_vertex method.
def test_add_vertex():
    g = Graph()
    assert g.add_vertex('A') is True  # Vertex A should be added
    assert 'A' in g.adj_list  # A should exist in the adjacency list
    assert g.add_vertex('A') is False  # Adding A again should return False

# Tests the add_edge method.
def test_add_edge(create_graph):
    g = create_graph
    assert g.add_edge('A', 'B') is True  # Edge A-B should exist
    assert 'B' in g.adj_list['A']  # B should be adjacent to A
    assert 'A' in g.adj_list['B']  # A should be adjacent to B
    assert g.add_edge('B', 'C') is True  # Add new edge B-C
    assert 'C' in g.adj_list['B']  # C should be adjacent to B
    assert 'B' in g.adj_list['C']  # B should be adjacent to C

# Tests adding an edge where one or both vertices do not exist.
def test_add_edge_with_nonexistent_vertex(create_graph):
    g = create_graph
    assert g.add_edge('A', 'D') is False  # D does not exist
    assert g.add_edge('X', 'Y') is False  # Both X and Y do not exist

# Tests the print_graph method to ensure correct output format.
def test_graph_print(capsys, create_graph):
    g = create_graph
    g.print_graph()
    captured = capsys.readouterr()
    assert captured.out == "A : ['B', 'C']\nB : ['A']\nC : ['A']\n"  # Check printed output
