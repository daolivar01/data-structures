class Graph:
    # Initializes an empty graph with an adjacency list.
    def __init__(self):
        self.adj_list = {}

    # Prints the graph, displaying each vertex and its adjacent vertices.
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    # Adds a new vertex to the graph if it doesn't already exist.
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Adds an undirected edge between two vertices if both exist in the graph.
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
